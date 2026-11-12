#!/usr/bin/env node
/**
 * Deterministic table drawer for writer's-room facts.
 *
 * The model does not choose names, places, trades, quirks or premise axes.
 * Code draws them from curated tables with a reproducible seed, then hands
 * the selected facts to the model as fixed canon.
 *
 * Usage:
 *   node tools/table-draw.mjs --seed wildy-001 --table names --count 3 --filter culture=grey-march
 *   node tools/table-draw.mjs --seed wildy-001 --table places --count 2
 *   node tools/table-draw.mjs --seed wildy-001 --table premise --count 3
 *   node tools/table-draw.mjs --seed wildy-001 --table names --list
 *   node tools/table-draw.mjs --seed wildy-001 --table names --json
 *
 * The seed is the story/quest/arc id, not the current time. Same seed + same
 * tables = same facts. Change the seed deliberately when you want a new draw.
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

const tablesPath = path.resolve(getArg('--tables', path.join(here, '..', 'templates', 'writers-room', 'TABLES.example.json')));
const data = JSON.parse(fs.readFileSync(tablesPath, 'utf8'));
const tables = data.tables ?? data;
const seed = getArg('--seed', 'default-seed');
const tableName = getArg('--table', 'names');
const count = Math.max(1, Number(getArg('--count', '1')) || 1);
const filters = args
  .map((arg, index) => (arg === '--filter' ? args[index + 1] : null))
  .filter(Boolean)
  .map((entry) => {
    const [key, ...rest] = entry.split('=');
    return [key, rest.join('=')];
  });
const excluded = new Set(
  (getArg('--exclude', '') || '')
    .split(',')
    .map((value) => value.trim().toLowerCase())
    .filter(Boolean),
);
const jsonOut = hasFlag('--json');
const listOut = hasFlag('--list');

// xmur3 + mulberry32: tiny deterministic PRNG, no dependencies.
function xmur3(str) {
  let h = 1779033703 ^ str.length;
  for (let i = 0; i < str.length; i += 1) {
    h = Math.imul(h ^ str.charCodeAt(i), 3432918353);
    h = (h << 13) | (h >>> 19);
  }
  return () => {
    h = Math.imul(h ^ (h >>> 16), 2246822507);
    h = Math.imul(h ^ (h >>> 13), 3266489909);
    return (h ^= h >>> 16) >>> 0;
  };
}
function mulberry32(a) {
  return () => {
    a |= 0;
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
const random = mulberry32(xmur3(seed)());

function matchesTags(item) {
  if (!filters.length) return true;
  return filters.every(([key, value]) => String(item.tags?.[key] ?? '') === value);
}
function isExcluded(item) {
  return excluded.has(String(item.value).toLowerCase()) || excluded.has(String(item.id).toLowerCase());
}
function weightedDraw(items) {
  const pool = items.filter((item) => matchesTags(item) && !isExcluded(item));
  const total = pool.reduce((sum, item) => sum + (Number(item.weight) || 1), 0);
  if (!pool.length || total <= 0) return null;
  let roll = random() * total;
  for (const item of pool) {
    roll -= Number(item.weight) || 1;
    if (roll <= 0) return item;
  }
  return pool[pool.length - 1];
}

function drawMany(items, amount) {
  const chosen = [];
  const used = new Set();
  for (let i = 0; i < amount; i += 1) {
    const pool = items.filter((item) => !used.has(item.id));
    const picked = weightedDraw(pool);
    if (!picked) break;
    used.add(picked.id);
    chosen.push(picked);
  }
  return chosen;
}

function clean(item) {
  return { id: item.id, value: item.value, tags: item.tags ?? {}, weight: item.weight ?? 1 };
}

if (listOut) {
  if (tableName === 'premise') {
    console.log(Object.keys(tables.premises ?? {}).join('\n'));
  } else {
    console.log((tables[tableName] ?? []).map((item) => `${item.id}\t${item.value}`).join('\n'));
  }
  process.exit(0);
}

if (!tables[tableName] && tableName !== 'premise') {
  console.error(`Unknown table: ${tableName}`);
  console.error(`Available: ${Object.keys(tables).filter((key) => key !== 'premises').join(', ')}, premise`);
  process.exit(1);
}

let result;
if (tableName === 'premise') {
  const axes = Object.entries(tables.premises ?? {});
  result = [];
  for (let i = 0; i < count; i += 1) {
    const bundle = { seed, bundle: i + 1, axes: {} };
    for (const [axis, items] of axes) {
      const picked = weightedDraw(items);
      if (picked) bundle.axes[axis] = clean(picked);
    }
    result.push(bundle);
  }
} else {
  result = drawMany(tables[tableName], count).map(clean);
}

if (jsonOut) {
  console.log(JSON.stringify({ seed, table: tableName, draws: result }, null, 2));
} else {
  console.log(`Seed: ${seed}`);
  console.log(`Table: ${tableName}`);
  console.log('');
  if (tableName === 'premise') {
    for (const bundle of result) {
      console.log(`Bundle ${bundle.bundle}`);
      for (const [axis, item] of Object.entries(bundle.axes)) {
        console.log(`  ${axis.padEnd(14)} ${item.value}`);
      }
      console.log('');
    }
  } else {
    for (const item of result) {
      console.log(`- ${item.value}  [${item.id}]`);
    }
  }
  console.log('Treat these as fixed facts. Do not let the model rename or replace them.');
}
