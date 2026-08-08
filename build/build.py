#!/usr/bin/env python3
"""
Build script for the med-spa portfolio.

Each page in build/src/ is authored once with a `/*__FONTS__*/` placeholder in
its <style>. This script injects the correct subset of base64-encoded @font-face
declarations (from build/fonts/fonts_b64.json) into each page and writes the
finished, fully self-contained HTML into ../site/.

Usage:
    python build.py            # build every page
    python build.py lumiere    # build only named page(s): portfolio|lumiere|sagesol|meridian
"""
import json, os, sys

HERE  = os.path.dirname(os.path.abspath(__file__))          # .../build
ROOT  = os.path.dirname(HERE)                                # repo root
SITE  = os.path.join(ROOT, "docs")                           # output (served by GitHub Pages)
FONTS = json.load(open(os.path.join(HERE, "fonts", "fonts_b64.json"), encoding="utf-8"))

def face(family, weight, style):
    b64 = FONTS["%s|%s|%s" % (family, weight, style)]
    return ("@font-face{font-family:'%s';font-style:%s;font-weight:%s;font-display:swap;"
            "src:url(data:font/woff2;base64,%s) format('woff2');}" % (family, style, weight, b64))

def css_for(specs):
    return "\n".join(face(*s) for s in specs)

# Which faces each page embeds (distinct type system per brand).
FONTSETS = {
    "portfolio": [
        ("Instrument Serif","400","normal"), ("Instrument Serif","400","italic"),
        ("Hanken Grotesk","400","normal"), ("Hanken Grotesk","500","normal"),
        ("Hanken Grotesk","600","normal"), ("Hanken Grotesk","700","normal"),
        ("Cormorant Garamond","600","normal"), ("Fraunces","600","normal"),
        ("Schibsted Grotesk","700","normal"),
    ],
    "lumiere": [
        ("Cormorant Garamond","500","normal"), ("Cormorant Garamond","600","normal"),
        ("Jost","300","normal"), ("Jost","400","normal"), ("Jost","500","normal"),
    ],
    "sagesol": [
        ("Fraunces","400","normal"), ("Fraunces","600","normal"),
        ("Instrument Sans","400","normal"), ("Instrument Sans","500","normal"),
        ("Instrument Sans","600","normal"),
    ],
    "meridian": [
        ("Schibsted Grotesk","400","normal"), ("Schibsted Grotesk","500","normal"),
        ("Schibsted Grotesk","700","normal"),
        ("Hanken Grotesk","400","normal"), ("Hanken Grotesk","500","normal"),
        ("Hanken Grotesk","600","normal"),
    ],
}

# src page -> output path (relative to repo root)
FILES = {
    "portfolio": ("src/portfolio.html",     os.path.join(SITE, "index.html")),
    "lumiere":   ("src/demo-lumiere.html",  os.path.join(SITE, "demos", "lumiere", "index.html")),
    "sagesol":   ("src/demo-sagesol.html",  os.path.join(SITE, "demos", "sage-sol", "index.html")),
    "meridian":  ("src/demo-meridian.html", os.path.join(SITE, "demos", "meridian", "index.html")),
}

def build(only=None):
    for key, (src, dest) in FILES.items():
        if only and key not in only:
            continue
        html = open(os.path.join(HERE, src), encoding="utf-8").read()
        html = html.replace("/*__FONTS__*/", css_for(FONTSETS[key]))
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "w", encoding="utf-8").write(html)
        print("built %-10s -> %s (%d KB)" % (key, os.path.relpath(dest, ROOT), len(html.encode()) // 1024))

if __name__ == "__main__":
    build(sys.argv[1:] or None)
