# AI-Made Websites That Don't Look Like They're Made by AI

**Three production-ready medical-spa websites and a portfolio landing page — designed with AI, then hardened by hand so nothing reads as "AI slop."** Every page is a single, self-contained HTML file: fonts embedded, zero build dependencies, zero third-party requests, instant load.

![Stack](https://img.shields.io/badge/stack-HTML%20%2F%20CSS%20%2F%20vanilla%20JS-1f2937?style=flat-square)
![Dependencies](https://img.shields.io/badge/runtime%20dependencies-0-16a34a?style=flat-square)
![Self-contained](https://img.shields.io/badge/fonts-inlined%20(offline%20ready)-7c3aed?style=flat-square)
![SEO](https://img.shields.io/badge/SEO%20%2B%20GEO-JSON--LD%20%2B%20FAQPage-0ea5e9?style=flat-square)
![A11y](https://img.shields.io/badge/a11y-WCAG%202.2%20AA--minded-b45309?style=flat-square)
![Mobile](https://img.shields.io/badge/layout-mobile--first-111827?style=flat-square)

---

## What this repository is

A focused portfolio built for one purpose: **building beautiful, conversion-optimized websites for medical spas using AI tools — without the generic "AI look."** It contains a portfolio landing page and three complete demo med-spa sites, each with a distinct brand identity but built from one shared component system, so every new site ships faster than the last.

The name is the whole thesis: anyone can prompt an AI into a website. The craft is removing every fingerprint afterward so it feels custom, premium, and human.

---

## The three demo builds

Three fictional med spas, three different treatment focuses, three completely different visual identities — one underlying system.

| # | Brand | Location | Focus | Visual identity |
|---|-------|----------|-------|-----------------|
| 01 | **Lumière Aesthetic Studio** | Scottsdale, AZ | Luxury injectables (Botox, filler, boosters) | Dark, editorial luxe · Cormorant Garamond + Jost · aubergine & champagne gold |
| 02 | **Sage & Sol Skin + Wellness** | Austin, TX | Skin health & IV wellness (facials, peels, drips) | Warm, botanical, bright · Fraunces + Instrument Sans · pine, sage & honey |
| 03 | **Meridian Body + Skin** | Denver, CO | Laser, body contouring & GLP-1 weight loss | Clinical-modern, results-driven · Schibsted Grotesk + Hanken Grotesk · ink, ice & teal |

Each site ships with: a sticky booking flow, transparent pricing, trust signals and reviews, a location/NAP block, an FAQ, and a "concept site" marker (the brands are invented — real client photography drops into the marked image slots).

---

## Live sites

The pages are static, so they run anywhere. After deploying (see **Deploy** below), the links are:

| Page | Path |
|------|------|
| Portfolio (home) | `https://<your-domain>/` |
| Lumière | `https://<your-domain>/demos/lumiere/` |
| Sage & Sol | `https://<your-domain>/demos/sage-sol/` |
| Meridian | `https://<your-domain>/demos/meridian/` |

Prefer to look first? See **Run locally** — it's two commands.

---

## Making AI output *not* look AI-made

The sites were deliberately built to avoid the well-documented "AI slop" tells. Each page was audited against a design-guidelines checklist and corrected:

| Common AI tell | What was done instead |
|----------------|-----------------------|
| **Inter / Roboto / Space Grotesk everywhere** | Distinctive display + body pairing per brand (Cormorant, Fraunces, Jost, Instrument, Schibsted, Hanken) — none of the default fonts |
| **Indigo→purple / SaaS-blue gradients** | Brand-semantic palettes; atmosphere from gradient *meshes* + SVG noise/grain, never a decorative purple gradient |
| **Three identical cards in a row** | Asymmetric **bento** service grids, **featured-first** reviews, a **diagonal** step sequence, staggered galleries |
| **Uniform 16px radius / 24px padding** | Varied, asymmetric corner radii and spacing to build hierarchy |
| **Thin-line icon atop every card** | Generic service icons removed; cards lead with the treatment name and price |
| **Fade-in on *every* element on scroll** | Replaced with a single, orchestrated staggered page-load intro on the hero only |
| **Robotic, hedge-y copy & em-dash tics** | Human, direct-response copy; every `—` removed and rewritten |
| **Accessibility as an afterthought** | Solid `:focus-visible` rings, real `<label>`s tied to inputs, `<main>` landmark, `prefers-reduced-motion`, contrast-checked text |

---

## SEO & GEO baked in

Med spas live on local discovery, so every page ships search-ready:

- **JSON-LD structured data** — `MedicalBusiness` / `HealthAndBeautyBusiness` with address, geo, opening hours, price range, `AggregateRating` and `OfferCatalog`.
- **`FAQPage` schema** — question-shaped content that AI search engines can cite (GEO / AI-citability).
- **Google Business Profile alignment** — consistent NAP (name, address, phone) and local keywords in headings and copy.
- **Performance** — self-contained, image-light, fonts inlined: fast first paint, no layout shift, no third-party bloat.

---

## How it's built — the system

The point is that these aren't one-offs. Each page is authored once in `build/src/` with a `/*__FONTS__*/` placeholder, and a small Python step injects the right subset of base64-embedded web fonts, writing the finished self-contained page into `site/`.

```
build/src/*.html   ──►   build/build.py   ──►   site/**/index.html
 (templated,           (injects embedded          (finished, fully
  fonts as a             @font-face faces          self-contained pages)
  placeholder)           per brand)
```

- **One component vocabulary** (header, hero, offer, services, reviews, FAQ, booking, footer) reused across every brand — a new client is a new palette, type system, and copy over a proven skeleton.
- **Fonts embedded as data-URIs** from `build/fonts/fonts_b64.json` (latin subset), so pages have no external font requests and render identically offline.
- **No framework, no bundler, no dependencies** beyond Python 3 for the build step.

---

## Run locally

No build needed to view — the files in `site/` are final. Just serve the folder:

```bash
cd site
python -m http.server 8000
```

Then open **http://localhost:8000/** (portfolio) and **http://localhost:8000/demos/lumiere/** etc. Opening the `.html` files directly in a browser also works.

---

## Rebuild / customize

To change copy, colors, or fonts, edit the templated sources and rebuild:

```bash
# edit build/src/demo-lumiere.html (or any page)
cd build
python build.py            # rebuild all pages into ../site
python build.py lumiere    # or just one: portfolio | lumiere | sagesol | meridian
```

Booking forms include a marked `<!-- GHL embed slot -->` where a Go High Level calendar/form drops in, and image zones are labeled for each client's own photography.

---

## Deploy

**Netlify (fastest, clean domain):** drag the `site/` folder onto <https://app.netlify.com/drop>, create a free account to keep it, then rename the site. Your pages are then at `https://<name>.netlify.app/`, `/demos/lumiere/`, etc.

**GitHub Pages (from this repo):** Settings → Pages → deploy from branch. Because the site lives in `/site`, pages resolve under `…/site/` (e.g. `https://<user>.github.io/<repo>/site/demos/lumiere/`). For a root-level Pages URL, deploy the `site/` folder on its own instead (Netlify is simpler for that).

---

## Repository structure

```
.
├── README.md
├── site/                        # the deployable static site (all pages final & self-contained)
│   ├── index.html               #   portfolio landing page
│   └── demos/
│       ├── lumiere/index.html   #   Demo 01 · luxury injectables
│       ├── sage-sol/index.html  #   Demo 02 · skin + IV wellness
│       └── meridian/index.html  #   Demo 03 · laser / body / weight-loss
└── build/                       # the reproducible build system
    ├── build.py                 #   injects embedded fonts, writes ../site
    ├── src/*.html               #   templated page sources (with font placeholder)
    └── fonts/fonts_b64.json     #   base64-embedded web fonts (latin subset)
```

---

## Notes

- **The med spas are fictional concept builds** — clearly labeled, with `.example` domains and `555` phone numbers. They demonstrate range and craft; they are not live businesses.
- **No generic stock photography** is used. The art-directed image slots are where a real client's photos go — avoiding clichéd stock is itself part of not looking AI-made.
- Built **AI-native and finished by hand**: fast to produce, deliberately edited so the result feels custom, premium, and human.
