#!/usr/bin/env python3
"""Render app/index.html to entry.png with headless Chrome, deterministically.

Usage: python3 render.py

- Opens the page at exactly 1024x1024 via file://.
- Waits for network idle + fonts + a settle delay so layout is complete.
- Writes entry.png in the repository root.
- Verifies: PNG magic bytes, 1024x1024 dimensions, size <= 1 MiB.
- Renders twice and compares; if byte-identical, prints OK (deterministic),
  otherwise keeps the first render and warns (Chrome variance).
"""
import hashlib
import os
import struct
import subprocess
import sys
import time

REPO = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(REPO, "app", "index.html")
OUT = os.path.join(REPO, "entry.png")
CHROME = "/usr/bin/google-chrome"
MAX_BYTES = 1_048_576


def render(dest: str) -> None:
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--force-device-scale-factor=1",
        "--window-size=1024,1024",
        "--no-sandbox",
        "--disable-lcd-text",           # keep text rasterisation stable across runs
        "--font-render-hinting=none",   # avoid hinting nondeterminism between runs
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=4000",   # let layout, fonts and SVG settle
        f"--screenshot={dest}",
        f"file://{PAGE}",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if proc.returncode != 0:
        print(proc.stderr[-2000:], file=sys.stderr)
        raise SystemExit(f"chrome exited {proc.returncode}")


def check(path: str) -> dict:
    with open(path, "rb") as f:
        data = f.read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("not a PNG")
    w, h = struct.unpack(">II", data[16:24])
    return {"bytes": len(data), "width": w, "height": h, "sha": hashlib.sha256(data).hexdigest()}


def main() -> None:
    tmp1 = os.path.join(REPO, ".render-a.png")
    tmp2 = os.path.join(REPO, ".render-b.png")

    render(tmp1)
    info = check(tmp1)
    print(f"render 1: {info['width']}x{info['height']}, {info['bytes']} bytes, sha256={info['sha'][:16]}...")
    assert info["width"] == 1024 and info["height"] == 1024, "wrong dimensions"
    assert info["bytes"] <= MAX_BYTES, f"over size cap: {info['bytes']} > {MAX_BYTES}"

    render(tmp2)
    info2 = check(tmp2)
    print(f"render 2: {info2['width']}x{info2['height']}, {info2['bytes']} bytes, sha256={info2['sha'][:16]}...")

    if info["sha"] == info2["sha"]:
        print("DETERMINISTIC: two renders are byte-identical")
        os.replace(tmp1, OUT)
        os.remove(tmp2)
    else:
        print("WARNING: Chrome added variance; keeping render 1 and noting it")
        os.replace(tmp1, OUT)
        os.remove(tmp2)

    final = check(OUT)
    print(f"entry.png written: {final['width']}x{final['height']}, {final['bytes']} bytes "
          f"({final['bytes']/MAX_BYTES:.1%} of cap)")


if __name__ == "__main__":
    main()
