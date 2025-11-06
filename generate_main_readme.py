"""
Combine all README.md files from subfolders into a single root README.md.

Behavior per requirements:
- Do NOT add headings based on folder names.
- For each README, convert its first non-empty line into a Markdown H1 heading
  if it does not already start with '#'.
- Lines like "# {...}" should be treated as raw text, not headings, by escaping '#'.
- Insert exactly one blank line between imported files.
- Output is written to the root-level README.md (overwriting if exists).
"""

from __future__ import annotations
import os
import re
from pathlib import Path

# Folders to skip entirely (extend as needed)
EXCLUDED_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".idea",
    ".vscode",
    "__pycache__",
    "node_modules",
    ".venv",
    "venv",
    ".mypy_cache",
    ".pytest_cache",
}


def is_excluded(dirname: str) -> bool:
    """Return True if directory name should be skipped."""
    name = os.path.basename(dirname)
    return name in EXCLUDED_DIRS


# Pattern to detect lines that would look like headings but are actually data,
# e.g. "# {'parni': ...}", "# [1, 2]", "# (tuple)", "# 'string'", '# "string"'
RAW_HASH_PATTERN = re.compile(r"^#\s*[\{\[\(\'\"].*")


def transform_readme_text(text: str) -> str:
    """
    - Make first non-empty line a '# ' heading if not already starting with '#'
    - Escape lines that match RAW_HASH_PATTERN so they render as raw text (not headings)
    """
    lines = text.splitlines()

    # 1) Promote first non-empty line to a heading if needed
    for i, line in enumerate(lines):
        if line.strip():  # found first non-empty
            if not line.lstrip().startswith("#"):
                lines[i] = "# " + line
            break

    # 2) Escape "hash-data" lines so they aren't rendered as headings
    for i, line in enumerate(lines):
        if RAW_HASH_PATTERN.match(line):
            lines[i] = "\\" + line  # prefix a backslash to the '#'

    return "\n".join(lines)


def main() -> None:
    root = Path(__file__).resolve().parent
    out_path = root / "README.md"

    # Find all README.md files (exclude the output README itself)
    readmes: list[Path] = []
    for r, dirs, files in os.walk(root):
        # prune dirs in-place
        dirs[:] = [d for d in dirs if not is_excluded(os.path.join(r, d))]
        rpath = Path(r)
        if "README.md" in files:
            p = rpath / "README.md"
            if p.resolve() != out_path.resolve():
                readmes.append(p)

    # Sort deterministically by relative path (case-insensitive)
    readmes.sort(key=lambda p: str(p.relative_to(root)).lower())

    parts: list[str] = []

    for p in readmes:
        try:
            content = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = p.read_text(errors="replace")

        transformed = transform_readme_text(content)
        parts.append(transformed.rstrip())  # strip trailing newlines for uniformity
        parts.append("")  # exactly one blank line separator

    # Write combined README (ensure single trailing newline)
    combined = "\n".join(parts).rstrip() + "\n"
    out_path.write_text(combined, encoding="utf-8")
    print(f"Wrote {out_path} with {len(readmes)} imported README(s).")


if __name__ == "__main__":
    main()
