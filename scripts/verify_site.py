"""Verify public-policy and local-reference invariants for the static site."""

from __future__ import annotations

from pathlib import Path
import re
import sys
from urllib.parse import unquote


REQUIRED_SECTIONS = ("education", "research", "skills", "publications", "notes")
PROHIBITED_PHRASES = (
    "unpublished model",
    "experimental result",
    "state-of-the-art",
)
REFERENCE_PATTERN = re.compile(r'''(?:href|src)\s*=\s*["']([^"']+)["']''', re.IGNORECASE)


def validate_site(root: Path) -> list[str]:
    """Return the public-site policy and local-reference errors under ``root``."""
    index_path = root / "index.html"
    if not index_path.is_file():
        return ["missing file: index.html"]

    contents = index_path.read_text(encoding="utf-8")
    lower_contents = contents.lower()
    errors = [
        f"missing section: {section}"
        for section in REQUIRED_SECTIONS
        if f'id="{section}"' not in lower_contents
        and f"id='{section}'" not in lower_contents
    ]

    if any(phrase in lower_contents for phrase in PROHIBITED_PHRASES):
        errors.append("prohibited public copy")

    archive_landing = root / "archive" / "index.html"
    if not archive_landing.is_file():
        errors.append("missing file: archive/index.html")
    else:
        archive_contents = archive_landing.read_text(encoding="utf-8").lower()
        if "legacy personal site" not in archive_contents:
            errors.append("archive landing lacks historical status")
        if "current professional homepage" not in archive_contents:
            errors.append("archive landing lacks current-home context")

    for reference in REFERENCE_PATTERN.findall(contents):
        target = _local_target(root, reference)
        if target is not None and not target.exists():
            errors.append(f"missing local reference: {reference}")

    return errors


def _local_target(root: Path, reference: str) -> Path | None:
    """Resolve one HTML reference when it denotes a local static-site path."""
    location = unquote(reference.split("#", maxsplit=1)[0].split("?", maxsplit=1)[0])
    if not location or location.startswith(("//", "data:", "mailto:", "tel:")):
        return None
    if re.match(r"^[a-z][a-z0-9+.-]*:", location, flags=re.IGNORECASE):
        return None
    if location.startswith("/"):
        return root / location.lstrip("/")
    return root / location


def main() -> int:
    """Print validation errors and return a conventional shell exit code."""
    errors = validate_site(Path.cwd())
    if not errors:
        return 0
    print("\n".join(errors))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
