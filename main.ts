// Entry program for news-image-20261126 r2 (Node 22, standard library only).
//
// The finished front page lives in this repo as entry.png, drawn on the
// builder's machine by render.py from the checked 26 November 2026 news
// brief documented in NOTES.md. The grader runs this program twice with
// no network, so all it does is put a byte-identical copy of that PNG at
// $MAKEFUN_OUTPUT_DIR/entry.png (or /output when that is unset), after
// confirming the bytes really start with the PNG signature.
//
// Run locally with:
//   mkdir -p ./out && MAKEFUN_OUTPUT_DIR=./out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

const source = new URL("./entry.png", import.meta.url);
const bytes = readFileSync(source);
const signature = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a];
for (let i = 0; i < signature.length; i++) {
  if (bytes[i] !== signature[i]) {
    throw new Error("entry.png is not a PNG file");
  }
}
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(outDir, "entry.png");
mkdirSync(outDir, { recursive: true });
copyFileSync(source, target);
console.log("wrote " + target + " (" + bytes.length + " bytes)");
