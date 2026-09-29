"""Behavioral tests for the dependency-free static-site verifier."""

from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.verify_site import REQUIRED_SECTIONS, validate_site


class ValidateSiteTests(unittest.TestCase):
    """Each test names the broken public-site condition it must catch."""

    def test_reports_missing_required_section(self) -> None:
        """Removing the education section must produce a clear validation error."""
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "index.html").write_text("<main></main>", encoding="utf-8")

            self.assertIn("missing section: education", validate_site(root))

    def test_reports_prohibited_research_copy(self) -> None:
        """Accidentally publishing an unpublished model claim must be rejected."""
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            sections = "".join(
                f'<section id="{section}"></section>'
                for section in REQUIRED_SECTIONS
            )
            (root / "index.html").write_text(
                sections + "unpublished model", encoding="utf-8"
            )

            self.assertIn("prohibited public copy", validate_site(root))


if __name__ == "__main__":
    unittest.main()
