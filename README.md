# Zhan Li — Academic Portfolio

This repository hosts the personal academic website of **Zhan Li**, a Ph.D.
student in Artificial Intelligence. It presents broad public interests in
quantum computing, machine learning, graph learning, scientific computing,
and open-source engineering.

The site is intentionally framework-free and deploys as a static GitHub Pages
website.

## Local preview

Run the following command from the repository root:

```bash
python3 -m http.server 8000 --directory .
```

Then open `http://localhost:8000/` in a browser. No dependency installation or
build step is required.

## Maintaining the current homepage

- Update public page content in [`index.html`](index.html).
- Update visual styles in [`assets/css/site.css`](assets/css/site.css).
- Run `python3 scripts/verify_site.py` before committing page changes.
- Run `python3 -m unittest discover -s tests -v` to execute the repository's
  static-site checks.

## Public content boundary

Only publish information that is already suitable for public release. Do not
add unpublished or in-progress project names, method details, model details,
datasets, experimental results, performance claims, or other non-public
research material.

Publications and notes should be added only when the material is publicly
available and can be described accurately.

## Legacy archive

The previous personal website is preserved under
[`archive/legacy-2021/`](archive/legacy-2021/). It remains in the repository
for historical continuity and should only be changed for preservation or a
narrowly scoped repair.
