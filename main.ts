// Entry program for news-image-20261126 r2 (Node 22, standard library only).
// The finished front page lives in this repo as entry.png. It was drawn on
// the builder's machine by render.py from the checked 26 November 2026
// news brief documented in NOTES.md. The grader runs this program twice
// with no network, so all it does is place a byte-identical copy of that
// PNG at $MAKEFUN_OUTPUT_DIR/entry.png (falling back to /output), after
// confirming the file really is a PNG.
// To try it yourself:
//   mkdir -p ./out && MAKEFUN_OUTPUT_DIR=./out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const PNG_MAGIC = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a];

const folder = dirname(fileURLToPath(import.meta.url));
const bytes = readFileSync(join(folder, 'entry.png'));
const head = [...bytes.subarray(0, PNG_MAGIC.length)];
if (head.join(',') !== PNG_MAGIC.join(',')) throw new Error('entry.png is not a PNG file');

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
const target = join(outDir, 'entry.png');
writeFileSync(target, bytes);
console.log(`entry.png (${bytes.length} bytes) -> ${target}`);
