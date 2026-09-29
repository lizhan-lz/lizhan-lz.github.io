# Research Portfolio Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the personal-site entry point with a professional, English-first academic portfolio while preserving all legacy content and Git history.

**Architecture:** Keep the site framework-free and deployable through GitHub Pages. The root will contain a semantic one-page site and focused assets; the 2021 personal website will move intact to `archive/legacy-2021/`, preserving its relative paths and original behaviour.

**Tech Stack:** HTML5, CSS3, standard-library Python `unittest`, Git, GitHub Pages.

**Spec:** `docs/superpowers/specs/2026-09-29-research-portfolio-design.md`

## Global Constraints

- Publish only broad, truthful academic information; never disclose unpublished or in-progress project names, methods, model details, datasets, results, or novelty claims.
- Do not alter core research code, delete historical assets, rewrite history, force-push, or add runtime third-party dependencies.
- Use the public name `Zhan Li` and English-first copy.
- Preserve legacy content unchanged under `archive/legacy-2021/`.
- Keep implementation commits small, independently reviewable, and verified before committing.
- Require action-time confirmation before changing public GitHub repository description or topics.

## Review Focus

- Root links and asset references must not point to an absent local file after archival.
- Root-page copy must omit prohibited unpublished-research language and quantitative claims.
- Navigation must remain usable at narrow widths without JavaScript.
- The archive landing page must identify the content as historical, not current.
- The repository must remain deployable as plain GitHub Pages static content without an install or build step.

---

## File Structure

| Path | Responsibility |
| --- | --- |
| `index.html` | Semantic root academic homepage and metadata. |
| `assets/css/site.css` | Responsive visual system for the root homepage only. |
| `archive/legacy-2021/` | Unmodified former root website and complete assets. |
| `archive/legacy-2021/README.md` | Historical-context notice and current-homepage link. |
| `README.md` | Repository purpose, public-content policy, preview, update, and archive guidance. |
| `.gitignore` | Excludes editor, OS, Python-cache, and local-preview artifacts. |
| `scripts/verify_site.py` | Dependency-free checks for required sections, prohibited copy, and local references. |
| `tests/test_verify_site.py` | Standard-library tests for the verifier. |

### Task 1: Preserve legacy assets and establish static checks

**Files:**
- Create: `.gitignore`, `archive/legacy-2021/README.md`, `scripts/verify_site.py`, `tests/test_verify_site.py`
- Move: `.idea/`, `css/`, `images/`, `js/`, `music/`, `photo/`, all root legacy `*.html`, `*.css`, `*.gif`, `*.jpg`, `*.mp3`, and `*.mp4` files to `archive/legacy-2021/`

**Interfaces:**
- Produces: `scripts.verify_site.validate_site(root: pathlib.Path) -> list[str]`; an empty list means the repository passes.
- Consumes: none.

- [ ] **Step 1: Write failing verifier tests in `tests/test_verify_site.py`**

```python
def test_validate_site_reports_missing_required_section(tmp_path: Path):
    (tmp_path / "index.html").write_text("<main></main>", encoding="utf-8")
    assert "missing section: education" in validate_site(tmp_path)

def test_validate_site_reports_prohibited_research_copy(tmp_path: Path):
    html = ''.join(f'<section id="{name}"></section>' for name in REQUIRED)
    (tmp_path / "index.html").write_text(html + "unpublished model", encoding="utf-8")
    assert "prohibited public copy" in validate_site(tmp_path)
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python3 -m unittest tests/test_verify_site.py -v`

Expected: FAIL because `scripts.verify_site` does not exist.

- [ ] **Step 3: Implement `validate_site(root: pathlib.Path) -> list[str]` in `scripts/verify_site.py`**

Use only `pathlib` and `re`. Check root `index.html` for IDs `education`, `research`, `skills`, `publications`, and `notes`; flag the case-insensitive phrases `unpublished model`, `experimental result`, and `state-of-the-art`; inspect non-external `href` and `src` references and report missing target files. Add a CLI that exits `1` when errors are returned.

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m unittest tests/test_verify_site.py -v`

Expected: PASS.

- [ ] **Step 5: Archive the old site and document its status**

Use `git mv` for every listed legacy item. Write the archive README stating that the files are a preserved 2021 personal website, are not the current professional homepage, and should only be changed for preservation or repair.

- [ ] **Step 6: Add repository hygiene and verify the archive**

Write `.gitignore` entries for `.DS_Store`, `Thumbs.db`, `.idea/`, `__pycache__/`, `*.py[cod]`, and `.python-version`. Run: `test -f archive/legacy-2021/index.html && python3 -m unittest tests/test_verify_site.py -v`.

Expected: archive entry point exists and tests PASS.

- [ ] **Step 7: Commit**

Run: `git add .gitignore archive scripts tests && git commit -m "chore: archive legacy personal site"`

### Task 2: Build the public academic homepage

**Files:**
- Create: `index.html`, `assets/css/site.css`
- Modify: `tests/test_verify_site.py`

**Interfaces:**
- Consumes: `validate_site(root: pathlib.Path) -> list[str]` from Task 1.
- Produces: a verified root homepage with required section IDs and a local stylesheet reference.

- [ ] **Step 1: Add a failing homepage integration test**

```python
def test_repository_homepage_passes_static_policy_checks():
    assert validate_site(Path(__file__).resolve().parents[1]) == []
```

- [ ] **Step 2: Run the integration test to verify it fails**

Run: `python3 -m unittest tests/test_verify_site.py -v`

Expected: FAIL because root `index.html` does not exist.

- [ ] **Step 3: Create semantic `index.html` and `assets/css/site.css`**

Create a `header` with text-only brand and anchor navigation; a `main` with IDs exactly `education`, `research`, `skills`, `publications`, and `notes`; and a `footer`. Set title to `Zhan Li | AI and Quantum Computing Researcher` with concise meta description. Use factual English-first copy; label Publications and Notes as public-work placeholders only. Exclude personal phone/email, legacy-media embeds, project names, methods, datasets, results, and performance claims.

Style using custom properties, system-font stack, visible focus state, and a `48rem` media query. Do not add JavaScript, external fonts, or CDNs.

- [ ] **Step 4: Run policy and link checks**

Run: `python3 scripts/verify_site.py && python3 -m unittest tests/test_verify_site.py -v`

Expected: verifier exits `0` and all tests PASS.

- [ ] **Step 5: Inspect local rendering**

Run: `python3 -m http.server 8000 --directory .`

Inspect `http://localhost:8000/` at desktop and narrow width. Confirm header, section headings, footer, readable line lengths, focus visibility, and navigation without overflow. Stop the server after inspection.

- [ ] **Step 6: Commit**

Run: `git add index.html assets/css/site.css tests/test_verify_site.py && git commit -m "feat: add academic research homepage"`

### Task 3: Document maintenance and update GitHub presentation metadata

**Files:**
- Create: `README.md`
- Modify: `tests/test_verify_site.py`
- External edit: GitHub repository description and topics for `lizhan-lz/lizhan-lz.github.io`

**Interfaces:**
- Consumes: verified static homepage and `validate_site(root: pathlib.Path) -> list[str]`.
- Produces: a documented site with accurate public GitHub discovery metadata.

- [ ] **Step 1: Add a failing documentation-presence test**

```python
def test_repository_documents_public_content_boundary_and_archive():
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "unpublished" in readme.lower()
    assert "archive/legacy-2021" in readme
```

- [ ] **Step 2: Run the documentation test to verify it fails**

Run: `python3 -m unittest tests/test_verify_site.py -v`

Expected: FAIL because `README.md` does not exist.

- [ ] **Step 3: Write `README.md`**

Describe the repository as Zhan Li's personal academic website; state the broad public themes; give `python3 -m http.server 8000 --directory .` for preview; identify `index.html` and `assets/css/site.css` as current-site update points; state the public-content boundary; and link to `archive/legacy-2021/`.

- [ ] **Step 4: Run all local checks**

Run: `python3 scripts/verify_site.py && python3 -m unittest discover -s tests -v && git diff --check`

Expected: verifier exits `0`, all unit tests PASS, and `git diff --check` has no output.

- [ ] **Step 5: Commit documentation**

Run: `git add README.md tests/test_verify_site.py && git commit -m "docs: document portfolio maintenance"`

- [ ] **Step 6: Update GitHub metadata after action-time confirmation**

Set description to `Academic portfolio and public notes on quantum computing, machine learning, graph learning, and scientific computing.` Set topics to `quantum-computing`, `machine-learning`, `graph-learning`, `scientific-computing`, and `research`. Do not add a website URL until the deployed root page is verified.

- [ ] **Step 7: Verify final repository state**

Run: `git status --short --branch && git log --oneline -4 && python3 scripts/verify_site.py && python3 -m unittest discover -s tests -v`

Expected: working tree clean, three focused implementation commits follow the design commit, verifier exits `0`, and all tests PASS.
