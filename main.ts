// news-world-20261120 entry program - Node 22, standard library only, no network.
// The front page image is pre-rendered and committed as entry.png beside this
// file (built from app/index.html by render.py with headless Chrome).
// At grade time the repository is mounted read-only at /bot and this program
// writes the image to /output/entry.png. MAKEFUN_OUTPUT_DIR stands in for
// /output when running locally.

import { mkdirSync, copyFileSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const src = fileURLToPath(new URL('./entry.png', import.meta.url));
const dst = join(outDir, 'entry.png');

mkdirSync(outDir, { recursive: true });
copyFileSync(src, dst);
