#!/usr/bin/env node
/**
 * Heuristic anti-slop audit.
 *
 * This is NOT an AI detector and NOT a banlist. It profiles text for known
 * slop patterns plus structural signals (sentence/paragraph variance, repetition,
 * em-dash density). Use it as a triage flag in CI and a conversation starter for
 * an editor; do not auto-reject work on a score alone.
 *
 * Usage:
 *   node tools/slop-audit.mjs --file scene.md
 *   node tools/slop-audit.mjs --root content/
 *   node tools/slop-audit.mjs --root content/ --json
 *   node tools/slop-audit.mjs --root content/ --fail-over 55
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const args = process.argv.slice(2);
const getArg = (flag, fallback) => {
  const index = args.indexOf(flag);
  return index >= 0 && args[index + 1] ? args[index + 1] : fallback;
};
const hasFlag = (flag) => args.includes(flag);

const patternsPath = path.resolve(getArg('--patterns', path.join(here, '..', 'data', 'slop-patterns.json')));
const patternData = JSON.parse(fs.readFileSync(patternsPath, 'utf8'));
const categories = patternData.categories ?? {};
const compiled = [];
for (const [category, entries] of Object.entries(categories)) {
  for (const entry of entries) {
    try {
      compiled.push({
        ...entry,
        category,
        regex: new RegExp(entry.pattern, 'gmi'),
      });
    } catch (error) {
      console.error(`Bad pattern ${entry.id}: ${error.message}`);
    }
  }
}

const fileArg = getArg('--file', '');
const rootArg = getArg('--root', '');
const jsonOut = hasFlag('--json');
const topN = Number(getArg('--top', '15')) || 15;
const failOver = Number(getArg('--fail-over', '-1'));
const skipDirs = new Set(['.git', 'node_modules', 'dist', 'build', '.next', 'coverage', 'vendor', '__pycache__', '.venv', 'venv']);
const extensions = new Set(['.md', '.txt', '.html', '.htm']);

function collectFiles(target) {
  if (!target) return [];
  const stat = fs.statSync(target);
  if (stat.isFile()) return [target];
  const files = [];
  for (const entry of fs.readdirSync(target, { withFileTypes: true })) {
    const full = path.join(target, entry.name);
    if (entry.isDirectory()) {
      if (!skipDirs.has(entry.name)) files.push(...collectFiles(full));
    } else if (entry.isFile() && extensions.has(path.extname(entry.name).toLowerCase())) {
      files.push(full);
    }
  }
  return files;
}

function mean(values) {
  return values.length ? values.reduce((a, b) => a + b, 0) / values.length : 0;
}
function stddev(values) {
  if (values.length < 2) return 0;
  const avg = mean(values);
  return Math.sqrt(mean(values.map((value) => (value - avg) ** 2)));
}

function auditText(text, file) {
  const words = text.trim() ? text.trim().split(/\s+/) : [];
  const wordCount = words.length;
  const sentences = text.split(/[.!?]+/).map((sentence) => sentence.trim()).filter(Boolean);
  const paragraphs = text.split(/\n\s*\n/).map((paragraph) => paragraph.trim()).filter(Boolean);
  const sentenceLengths = sentences.map((sentence) => sentence.split(/\s+/).length);
  const paragraphLengths = paragraphs.map((paragraph) => paragraph.split(/\s+/).length);
  const lowerWords = words.map((word) => word.toLowerCase().replace(/[^a-z'-]/g, '')).filter(Boolean);
  const uniqueRatio = lowerWords.length ? new Set(lowerWords).size / lowerWords.length : 0;
  const emDashes = (text.match(/—/g) ?? []).length;
  const semicolons = (text.match(/;/g) ?? []).length;

  const hits = [];
  let weightedHits = 0;
  const categoryCounts = {};
  const categoryWeights = {};
  for (const pattern of compiled) {
    pattern.regex.lastIndex = 0;
    const matches = text.match(pattern.regex);
    if (!matches || matches.length === 0) continue;
    const weight = Number(pattern.weight) || 1;
    const count = matches.length;
    hits.push({ id: pattern.id, category: pattern.category, count, weight, note: pattern.note ?? '' });
    weightedHits += weight * count;
    categoryCounts[pattern.category] = (categoryCounts[pattern.category] ?? 0) + count;
    categoryWeights[pattern.category] = (categoryWeights[pattern.category] ?? 0) + weight * count;
  }
  hits.sort((a, b) => b.weight * b.count - a.weight * a.count);

  const per1k = (value) => (wordCount ? (value / wordCount) * 1000 : 0);
  const weightedPer1k = per1k(weightedHits);
  const score = Math.min(100, Math.round(weightedPer1k * 2));
  const trigramCounts = new Map();
  for (let i = 0; i + 2 < lowerWords.length; i += 1) {
    const key = `${lowerWords[i]} ${lowerWords[i + 1]} ${lowerWords[i + 2]}`;
    trigramCounts.set(key, (trigramCounts.get(key) ?? 0) + 1);
  }
  const repeatedTrigrams = [...trigramCounts.entries()]
    .filter(([, count]) => count >= 3)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 5)
    .map(([trigram, count]) => ({ trigram, count }));

  return {
    file,
    words: wordCount,
    sentences: sentences.length,
    paragraphs: paragraphs.length,
    avgSentenceWords: Number(mean(sentenceLengths).toFixed(1)),
    sentenceLengthStdDev: Number(stddev(sentenceLengths).toFixed(1)),
    avgParagraphWords: Number(mean(paragraphLengths).toFixed(1)),
    paragraphLengthStdDev: Number(stddev(paragraphLengths).toFixed(1)),
    uniqueRatio: Number(uniqueRatio.toFixed(2)),
    emDashes,
    semicolons,
    emDashesPer1k: Number(per1k(emDashes).toFixed(1)),
    weightedHits,
    weightedPer1k: Number(weightedPer1k.toFixed(1)),
    score,
    categoryCounts,
    categoryWeights,
    topHits: hits.slice(0, topN),
    repeatedTrigrams,
  };
}

const target = fileArg || rootArg;
if (!target) {
  console.error('Provide --file <path> or --root <directory>.');
  process.exit(1);
}
const files = collectFiles(path.resolve(target));
if (!files.length) {
  console.error('No .md/.txt/.html files found.');
  process.exit(1);
}
const reports = files.map((file) => auditText(fs.readFileSync(file, 'utf8'), file));
const aggregate = reports.length === 1 ? reports[0] : (() => {
  const words = reports.reduce((sum, report) => sum + report.words, 0);
  const weightedHits = reports.reduce((sum, report) => sum + report.weightedHits, 0);
  const weightedPer1k = words ? (weightedHits / words) * 1000 : 0;
  const average = (key) => Number((reports.reduce((sum, report) => sum + (report[key] || 0), 0) / reports.length).toFixed(1));
  return {
    file: path.resolve(target),
    files: reports.length,
    words,
    sentences: reports.reduce((sum, report) => sum + report.sentences, 0),
    paragraphs: reports.reduce((sum, report) => sum + report.paragraphs, 0),
    avgSentenceWords: average('avgSentenceWords'),
    sentenceLengthStdDev: average('sentenceLengthStdDev'),
    avgParagraphWords: average('avgParagraphWords'),
    paragraphLengthStdDev: average('paragraphLengthStdDev'),
    uniqueRatio: average('uniqueRatio'),
    emDashes: reports.reduce((sum, report) => sum + report.emDashes, 0),
    semicolons: reports.reduce((sum, report) => sum + report.semicolons, 0),
    emDashesPer1k: Number((reports.reduce((sum, report) => sum + report.emDashes, 0) / Math.max(1, words) * 1000).toFixed(1)),
    weightedHits,
    weightedPer1k: Number(weightedPer1k.toFixed(1)),
    score: Math.min(100, Math.round(weightedPer1k * 2)),
    categoryCounts: reports.reduce((acc, report) => {
      for (const [key, value] of Object.entries(report.categoryCounts)) acc[key] = (acc[key] ?? 0) + value;
      return acc;
    }, {}),
    categoryWeights: reports.reduce((acc, report) => {
      for (const [key, value] of Object.entries(report.categoryWeights)) acc[key] = (acc[key] ?? 0) + value;
      return acc;
    }, {}),
    worst: [...reports].sort((a, b) => b.score - a.score).slice(0, 5).map(({ file, score, words }) => ({ file, score, words })),
    topHits: reports.flatMap((report) => report.topHits).sort((a, b) => b.weight * b.count - a.weight * a.count).slice(0, topN),
  };
})();

if (jsonOut) {
  console.log(JSON.stringify({ target, aggregate, reports }, null, 2));
} else {
  console.log(`Slop audit (heuristic): ${aggregate.file}`);
  if (aggregate.files) console.log(`Files: ${aggregate.files} · words: ${aggregate.words}`);
  console.log(`Score: ${aggregate.score}/100 · weighted hits/1k: ${aggregate.weightedPer1k}`);
  if (aggregate.words) {
    console.log(`Sentences: avg ${aggregate.avgSentenceWords} words, stddev ${aggregate.sentenceLengthStdDev}`);
    console.log(`Paragraphs: avg ${aggregate.avgParagraphWords} words, stddev ${aggregate.paragraphLengthStdDev}`);
    console.log(`Unique-word ratio: ${aggregate.uniqueRatio} · em dashes: ${aggregate.emDashes} (${aggregate.emDashesPer1k}/1k)`);
  }
  console.log('');
  console.log('Top patterns:');
  for (const hit of aggregate.topHits) {
    console.log(`- ${hit.category}/${hit.id}: ${hit.count} (weight ${hit.weight})${hit.note ? ` — ${hit.note}` : ''}`);
  }
  if (aggregate.worst) {
    console.log('');
    console.log('Worst files:');
    for (const report of aggregate.worst) console.log(`- ${report.file}: ${report.score}/100 (${report.words} words)`);
  }
  console.log('');
  console.log('This is a triage signal, not a verdict. Do not auto-reject on score alone.');
}

if (failOver >= 0 && aggregate.score > failOver) process.exit(1);
