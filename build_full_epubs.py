#!/usr/bin/env python3
"""
Build iPhone-friendly EPUB files from full-book markdown sources.
"""

from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path

import markdown
from ebooklib import epub


BASE_DIR = Path(__file__).resolve().parent


@dataclass(frozen=True)
class FullBookSpec:
    source: Path
    output: Path
    title: str
    identifier: str
    author: str
    chapter_heading_prefix: str


SPECS: tuple[FullBookSpec, ...] = (
    FullBookSpec(
        source=BASE_DIR / "book1" / "full_book.md",
        output=BASE_DIR / "book1" / "full_book_iPhone.epub",
        title="Rachel's Journey",
        identifier="rachel-journey-book1-full",
        author="Braden",
        chapter_heading_prefix="## Chapter ",
    ),
    FullBookSpec(
        source=BASE_DIR / "book2" / "Book2_full.md",
        output=BASE_DIR / "book2" / "Book2_full_iPhone.epub",
        title="Rachel Isekai — Book 2",
        identifier="rachel-isekai-book2-full",
        author="Braden",
        chapter_heading_prefix="# Chapter ",
    ),
)


def split_into_chapters(markdown_text: str, chapter_heading_prefix: str) -> list[tuple[str, str]]:
    lines = markdown_text.splitlines()
    chapter_starts = [
        idx for idx, line in enumerate(lines) if line.startswith(chapter_heading_prefix)
    ]
    if not chapter_starts:
        raise RuntimeError(f"No chapter headings found with prefix: {chapter_heading_prefix!r}")

    chapters: list[tuple[str, str]] = []
    for chapter_index, start in enumerate(chapter_starts):
        end = (
            chapter_starts[chapter_index + 1]
            if chapter_index + 1 < len(chapter_starts)
            else len(lines)
        )
        chunk = lines[start:end]
        heading = chunk[0].lstrip("#").strip()
        body_markdown = "\n".join(chunk[1:]).strip()
        chapters.append((heading, body_markdown))

    return chapters


def build_epub(spec: FullBookSpec) -> None:
    markdown_text = spec.source.read_text(encoding="utf-8")
    chapters = split_into_chapters(markdown_text, spec.chapter_heading_prefix)

    book = epub.EpubBook()
    book.set_identifier(spec.identifier)
    book.set_title(spec.title)
    book.set_language("en")
    book.add_author(spec.author)

    css = epub.EpubItem(
        uid="style",
        file_name="style/iphone.css",
        media_type="text/css",
        content=(
            "body { font-family: serif; line-height: 1.45; margin: 0 5%; }"
            "h1 { margin-top: 0; }"
        ),
    )
    book.add_item(css)

    epub_chapters: list[epub.EpubHtml] = []
    for chapter_number, (chapter_title, chapter_body_md) in enumerate(chapters, start=1):
        chapter_html = markdown.markdown(chapter_body_md, extensions=["extra"])
        chapter_item = epub.EpubHtml(
            title=chapter_title,
            file_name=f"chapter_{chapter_number:03d}.xhtml",
            lang="en",
        )
        chapter_item.content = f"<h1>{escape(chapter_title)}</h1>\n{chapter_html}"
        chapter_item.add_item(css)
        book.add_item(chapter_item)
        epub_chapters.append(chapter_item)

    book.toc = tuple(epub_chapters)
    book.spine = ["nav", *epub_chapters]
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    spec.output.parent.mkdir(parents=True, exist_ok=True)
    epub.write_epub(str(spec.output), book, {})


def main() -> None:
    for spec in SPECS:
        if not spec.source.exists():
            raise FileNotFoundError(f"Missing markdown source: {spec.source}")
        build_epub(spec)
        print(f"Wrote epub: {spec.output}")


if __name__ == "__main__":
    main()
