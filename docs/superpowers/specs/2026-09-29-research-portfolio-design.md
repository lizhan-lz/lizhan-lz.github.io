# Research Portfolio Redesign

## Purpose

Transform `lizhan-lz.github.io` from a personal 2021 static site into an
English-first public research portfolio for Zhan Li, a Ph.D. student in
Artificial Intelligence. The site should communicate broad interests in
quantum computing, machine learning, graph learning, scientific computing,
and open-source engineering.

## Scope and public-information boundary

The redesign contains only general, public-facing academic information. It
must not disclose unpublished or in-progress project names, methods, model
details, experimental results, datasets, or claims of research novelty.

The work is limited to documentation, presentation, and file organisation. It
does not modify core research code or delete historical assets.

## Information architecture

The new `index.html` is a single-page, responsive research homepage with these
sections:

1. **Introduction** — name, role, short broad research statement, and links.
2. **Education** — concise chronological academic background.
3. **Research interests** — Quantum Computing, Machine Learning, Graph
   Learning, and Scientific Computing, described at a high level.
4. **Technical skills** — programming, scientific-computing, and quantum
   software ecosystems, without overstating proficiency.
5. **Publications** — a clearly labelled placeholder for peer-reviewed and
   public preprint entries only.
6. **Notes / Blog** — a clearly labelled placeholder for future public notes.

The main navigation links to these sections. A compact footer includes the
repository and GitHub Pages attribution.

## Visual and engineering approach

The site will remain framework-free static HTML, CSS, and minimal JavaScript.
This avoids a toolchain migration and keeps GitHub Pages deployment simple.
The visual direction is restrained and academic: readable typography, strong
contrast, responsive spacing, accessible navigation, and no decorative audio
or autoplay content.

Shared public assets will be placed under `assets/`. The homepage will use
semantic HTML and avoid third-party runtime dependencies. Page metadata will
include a meaningful English title and description suitable for search and
link previews.

## Legacy preservation

The existing personal pages and their assets will be preserved intact under
`archive/legacy-2021/`. Their content will not be rewritten. A short archive
README will state their historical status and point visitors to the new
homepage.

## Repository documentation and metadata

A root `README.md` will describe the site purpose, its public-information
boundary, local preview instructions, content update locations, and the legacy
archive. `.gitignore` will prevent editor and operating-system files from
being added in future commits.

Repository description and topics will be updated to broad, truthful public
categories. The exact topics will exclude unpublished project identifiers and
performance claims.

## Verification and delivery

Before each commit, verify that internal links resolve, the HTML contains no
unpublished project references, and the working tree contains only intended
files. Test the static site locally using an HTTP server and inspect its
desktop and narrow-screen layout. Commits remain small and independently
reviewable:

1. legacy archive and base repository hygiene;
2. research homepage and supporting assets;
3. documentation and GitHub repository metadata.

No deletion, force-push, or history rewrite is permitted.
