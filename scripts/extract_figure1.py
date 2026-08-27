#!/usr/bin/env python3
"""Best-effort Figure-1 extractor for local paper PDFs.

Usage:
    python scripts/extract_figure1.py papers/2606.05660.pdf assets/figures/02_safe-embodied-ai.png

It locates a caption containing "Figure 1" / "Fig. 1" and renders the region above it.
Manual adjustment may still be needed for multi-column or unusual layouts.
"""
import sys, re
from pathlib import Path
import fitz

if len(sys.argv) != 3:
    raise SystemExit("Usage: extract_figure1.py INPUT.pdf OUTPUT.png")

pdf, out = Path(sys.argv[1]), Path(sys.argv[2])
doc = fitz.open(pdf)
patterns = [re.compile(r"^\s*Figure\s*1\b", re.I), re.compile(r"^\s*Fig\.?\s*1\b", re.I)]
found = None
for page in doc:
    blocks = page.get_text("blocks")
    for b in blocks:
        text = b[4].strip().replace("\n", " ")
        if any(p.search(text) for p in patterns):
            found = (page, fitz.Rect(b[:4]), text)
            break
    if found: break

if not found:
    raise SystemExit("Could not locate a Figure 1 caption automatically.")

page, cap, text = found
# Heuristic: most academic figure captions are below the figure.
y1 = max(0, cap.y0 - 4)
y0 = max(0, y1 - page.rect.height * 0.48)
clip = fitz.Rect(0, y0, page.rect.width, y1)
pix = page.get_pixmap(matrix=fitz.Matrix(2.2, 2.2), clip=clip, alpha=False)
out.parent.mkdir(parents=True, exist_ok=True)
pix.save(out)
print(f"Saved {out} from page {page.number+1}; caption: {text[:100]}")
