#!/usr/bin/env python3
"""
Build canonical full-book outputs for Book 2:
- Book2_full.md
- Book2_full.epub
"""

from __future__ import annotations

import re
from pathlib import Path

import markdown
from ebooklib import epub


BASE_DIR = Path(__file__).resolve().parent


def canonical_chapter_paths() -> list[Path]:
    part1 = {
        1: "Book2_Chapter1_Draft1.md",
        2: "Book2_Chapter2_Draft1.md",
        3: "Book2_Chapter3_Draft1.md",
        4: "Book2_Chapter4_Draft1.md",
        5: "Book2_Chapter5_Draft1.md",
        6: "Book2_Chapter6_Draft1.md",
        7: "Book2_Chapter7_Draft1.md",
        8: "Book2_Chapter8_Draft1.md",
        9: "Book2_Chapter9_Draft2.md",
        10: "Book2_Chapter10_Draft1.md",
        11: "Book2_Chapter11_Draft2.md",
        12: "Book2_Chapter12.md",
        13: "Book2_Chapter13.md",
        14: "Book2_Chapter14.md",
        15: "Book2_Chapter15_REVISED.md",
        16: "Book2_Chapter16_REVISED.md",
        17: "Book2_Chapter17_REVISED.md",
        18: "Book2_Chapter18.md",
        19: "Book2_Chapter19.md",
        20: "Book2_Chapter20.md",
    }

    chapter_files: list[Path] = []
    for number in range(1, 21):
        chapter_files.append(BASE_DIR / "part1" / part1[number])
    for number in range(21, 36):
        chapter_files.append(BASE_DIR / "part2" / f"Book2_Chapter{number}.md")
    for number in range(36, 44):
        chapter_files.append(BASE_DIR / "part3" / f"Book2_Chapter{number}.md")

    return chapter_files


def extract_heading(markdown_text: str) -> str:
    for line in markdown_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Untitled Chapter"


def combine_markdown(chapter_paths: list[Path], output_path: Path) -> None:
    parts: list[str] = ["# Rachel Isekai — Book 2", ""]

    for idx, chapter_path in enumerate(chapter_paths):
        if not chapter_path.exists():
            raise FileNotFoundError(f"Missing chapter file: {chapter_path}")
        chapter_text = chapter_path.read_text(encoding="utf-8")
        parts.append(chapter_text.strip())
        if idx < len(chapter_paths) - 1:
            parts.append("\n---\n")

    output_path.write_text("\n\n".join(parts).rstrip() + "\n", encoding="utf-8")


def build_epub(chapter_paths: list[Path], output_path: Path) -> None:
    book = epub.EpubBook()
    book.set_identifier("rachel-isekai-book2")
    book.set_title("Rachel Isekai — Book 2")
    book.set_language("en")
    book.add_author("Braden")

    epub_chapters: list[epub.EpubHtml] = []

    for i, chapter_path in enumerate(chapter_paths, start=1):
        md_text = chapter_path.read_text(encoding="utf-8")
        heading = extract_heading(md_text)

        # Keep chapter heading in body for context; iPhone readers handle this well.
        html_body = markdown.markdown(md_text, extensions=["extra"])

        epub_chapter = epub.EpubHtml(
            title=heading,
            file_name=f"chapter_{i:02d}.xhtml",
            lang="en",
        )
        epub_chapter.content = f"<h1>{heading}</h1>\n{html_body}"
        book.add_item(epub_chapter)
        epub_chapters.append(epub_chapter)

    book.toc = tuple(epub_chapters)
    book.spine = ["nav", *epub_chapters]
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    epub.write_epub(str(output_path), book, {})


def main() -> None:
    chapter_paths = canonical_chapter_paths()
    if len(chapter_paths) != 43:
        raise RuntimeError(f"Expected 43 chapters, found {len(chapter_paths)}")

    # Validate chapter headers include titles.
    missing_titles: list[Path] = []
    title_pattern = re.compile(r"^#\s*Chapter\s+\d+\s*[—-]{1,2}\s+.+$")
    for chapter_path in chapter_paths:
        first_line = chapter_path.read_text(encoding="utf-8").splitlines()[0].strip()
        if not title_pattern.match(first_line):
            missing_titles.append(chapter_path)
    if missing_titles:
        joined = "\n".join(str(p) for p in missing_titles)
        raise RuntimeError(f"Some chapters are missing titled headers:\n{joined}")

    md_output = BASE_DIR / "Book2_full.md"
    epub_output = BASE_DIR / "Book2_full.epub"

    combine_markdown(chapter_paths, md_output)
    build_epub(chapter_paths, epub_output)

    print(f"Wrote markdown: {md_output}")
    print(f"Wrote epub: {epub_output}")


if __name__ == "__main__":
    main()

