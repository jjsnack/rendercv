#!/usr/bin/env python3
"""Render the CV with the largest line spacing that still fits on one page.

Usage: python fit.py CV.yaml [--min 0.5] [--max 0.85] [--out DIR]

Output (PDF, PNG, .typ unless the YAML's settings say otherwise) goes to --out,
by default a build/ folder next to the YAML.
"""
import argparse
import pathlib
import subprocess
import sys

ap = argparse.ArgumentParser()
ap.add_argument("cv", type=pathlib.Path)
ap.add_argument("--min", type=float, default=0.5, help="tightest line spacing in em, tried first")
ap.add_argument("--max", type=float, default=0.85, help="never go looser than this (em)")
ap.add_argument("--out", type=pathlib.Path, help="output folder (default: build/ next to the YAML)")
args = ap.parse_args()

out = (args.out or args.cv.resolve().parent / "build").resolve()


def render(spacing: float) -> int:
    """Render at `spacing` em and return the page count."""
    for png in out.glob("*.png"):
        png.unlink()
    cmd = [
        sys.executable, "-m", "rendercv", "render", args.cv, "-q",
        "--output-folder", str(out), "--design.typography.line_spacing", f"{spacing:.3f}em",
    ]
    subprocess.run(cmd, check=True)
    return len(list(out.glob("*.png")))


# shortcut: bisection assumes page count never decreases as spacing grows, true for plain flow content.
lo, hi = args.min, args.max
if render(lo) > 1:
    raise SystemExit(f"Doesn't fit on one page even at {lo}em; trim content or shrink other spacing.")
if render(hi) == 1:
    lo = hi
else:
    while hi - lo > 0.005:
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if render(mid) == 1 else (lo, mid)

render(lo)
print(f"line_spacing: {lo:.3f}em (one page) -> {out}/")
