#!/usr/bin/env node
/**
 * Portfolio name audit.
 *
 * Counts a curated set of names across a directory tree, reports concentration
 * and cross-project reuse, and highlights names that are already doing the same
 * job in more than one game.
 *
 * Usage:
 *   node tools/name-audit.mjs --root /path/to/projects
 *   node tools/name-audit.mjs --root . --json
 *   node tools/name-audit.mjs --root . --registry data/name-commons.json
 *
 * No dependencies. Case-sensitive so ordinary words ("Ash") do not swamp the
 * result. This is a heuristic, not a full NLP name extractor.
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

const root = path.resolve(getArg('--root', process.cwd()));
const registryPath = path.resolve(here, '..', getArg('--registry', 'data/name-commons.json'));
const jsonOut = args.includes('--json');
const topN = Number(getArg('--top', '20')) || 20;

const registry = JSON.parse(fs.readFileSync(registryPath, 'utf8'));
const names = [...new Set(registry.names.map((entry) => (typeof entry === 'string' ? entry : entry.name)).filter(Boolean))];
const meta = new Map(
  registry.names
    .filter((entry) => typeof entry !== 'string')
    .map((entry) => [entry.name, entry]),
);

const skipDirs = new Set([
  '.git', 'node_modules', 'dist', 'build', '.next', 'coverage', 'vendor',
  '__pycache__', '.venv', 'venv', 'Pods', 'DerivedData', '.turbo', '.cache',
]);
const textExtensions = new Set([
  '.md', '.txt', '.js', '.mjs', '.cjs', '.ts', '.tsx', '.jsx', '.json',
  '.html', '.htm', '.css', '.py', '.yaml', '.yml', '.csv',
]);
const MAX_BYTES = 2 * 1024 * 1024;

const results = new Map(names.map((name) => [name, { name, total: 0, files: new Map(), projects: new Map() }]));
const rootIsRepo = fs.existsSync(path.join(root, '.git')) || fs.existsSync(path.join(root, 'package.json'));
const rootProject = path.basename(root);

function escapeRegExp(value) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}
const patterns = new Map(names.map((name) => [name, new RegExp(`\\b${escapeRegExp(name)}\\b`, 'g')]));

function walk(directory) {
  let entries;
  try {
    entries = fs.readdirSync(directory, { withFileTypes: true });
  } catch {
    return;
  }
  for (const entry of entries) {
    if (entry.isDirectory()) {
      if (!skipDirs.has(entry.name)) walk(path.join(directory, entry.name));
      continue;
    }
    if (!entry.isFile()) continue;
    const ext = path.extname(entry.name).toLowerCase();
    if (!textExtensions.has(ext)) continue;
    const filePath = path.join(directory, entry.name);
    let stat;
    try {
      stat = fs.statSync(filePath);
    } catch {
      continue;
    }
    if (stat.size > MAX_BYTES) continue;
    let text;
    try {
      text = fs.readFileSync(filePath, 'utf8');
    } catch {
      continue;
    }
    const relative = path.relative(root, filePath);
    if (relative.startsWith('..')) continue;
    const project = rootIsRepo
      ? rootProject
      : relative.includes(path.sep)
        ? relative.split(path.sep)[0]
        : '(root)';
    for (const [name, pattern] of patterns) {
      pattern.lastIndex = 0;
      const matches = text.match(pattern);
      if (!matches || matches.length === 0) continue;
      const record = results.get(name);
      record.total += matches.length;
      record.files.set(relative, (record.files.get(relative) || 0) + matches.length);
      record.projects.set(project, (record.projects.get(project) || 0) + matches.length);
    }
  }
}

walk(root);

const found = [...results.values()].filter((record) => record.total > 0).sort((a, b) => b.total - a.total);
const totalHits = found.reduce((sum, record) => sum + record.total, 0);
const collision = totalHits > 0
  ? found.reduce((sum, record) => sum + (record.total / totalHits) ** 2, 0)
  : 0;
const top10 = found.slice(0, 10).reduce((sum, record) => sum + record.total, 0);
const crossProject = found.filter((record) => record.projects.size > 1);

const output = {
  root,
  registry: registryPath,
  namesTracked: names.length,
  namesFound: found.length,
  totalHits,
  collisionProbability: Number(collision.toFixed(4)),
  top10Share: totalHits ? Number((top10 / totalHits).toFixed(4)) : 0,
  top: found.slice(0, topN).map((record) => ({
    name: record.name,
    hits: record.total,
    projects: [...record.projects.entries()].sort((a, b) => b[1] - a[1]),
    topFiles: [...record.files.entries()].sort((a, b) => b[1] - a[1]).slice(0, 5),
    status: meta.get(record.name)?.status ?? 'unregistered',
    decision: meta.get(record.name)?.decision ?? '',
  })),
  crossProject: crossProject.map((record) => ({
    name: record.name,
    hits: record.total,
    projects: [...record.projects.entries()].sort((a, b) => b[1] - a[1]),
    decision: meta.get(record.name)?.decision ?? '',
  })),
};

if (jsonOut) {
  console.log(JSON.stringify(output, null, 2));
} else {
  console.log(`Name audit: ${root}`);
  console.log(`Tracked ${names.length} names · found ${found.length} · ${totalHits} occurrences`);
  console.log(`Collision probability: ${output.collisionProbability} · top-10 share: ${(output.top10Share * 100).toFixed(1)}%`);
  console.log('');
  console.log('NAME'.padEnd(14), 'HITS'.padStart(5), 'PROJECTS'.padEnd(38), 'STATUS');
  for (const row of output.top) {
    const projects = row.projects.map(([project, hits]) => `${project}(${hits})`).join(', ');
    console.log(row.name.padEnd(14), String(row.hits).padStart(5), projects.slice(0, 38).padEnd(38), row.status);
  }
  if (output.crossProject.length) {
    console.log('');
    console.log('Cross-project names:');
    for (const row of output.crossProject) {
      console.log(`- ${row.name}: ${row.projects.map(([project, hits]) => `${project}(${hits})`).join(', ')}`);
      if (row.decision) console.log(`  ${row.decision}`);
    }
  }
  console.log('');
  console.log('Note: heuristic, not a full name extractor. Use it to find drift, not to ban real names.');
}
