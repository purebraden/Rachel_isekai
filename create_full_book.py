#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Combine all Rachel Isekai chapters into a single markdown file and EPUB.
"""

import os
import re
from pathlib import Path
from ebooklib import epub
import markdown

def get_chapter_files():
    """Get all chapter files in order."""
    base_dir = Path(__file__).parent
    
    # Define chapters in order
    chapters = []
    
    # Part 1: Chapters 1-14
    part1_files = [
        "Rachel_Isekai_Chapter1_PATCHED-2.md",
        "Rachel_Isekai_Chapter2_PATCHED-2.md",
        "Rachel_Isekai_Chapter3_ASCII-2.md",
        "Rachel_Isekai_Chapter4_FINAL-2.md",
        "Rachel_Isekai_Chapter5_FINAL-2.md",
        "Rachel_Isekai_Chapter6_REVISED-2.md",
        "Rachel_Isekai_Chapter7_FINAL-2.md",
        "Rachel_Isekai_Chapter8_HUMANIZED.md",
        "Rachel_Isekai_Chapter9_HUMANIZED.md",
        "Rachel_Isekai_Chapter10_HUMANIZED.md",
        "Rachel_Isekai_Chapter11_HUMANIZED.md",
        "Rachel_Isekai_Chapter12_HUMANIZED.md",
        "Rachel_Isekai_Chapter13_HUMANIZED.md",
        "Rachel_Isekai_Chapter14_HUMANIZED.md",
    ]
    
    for filename in part1_files:
        chapters.append(base_dir / "part1" / filename)
    
    # Part 2: Chapters 15-28
    for i in range(15, 29):
        chapters.append(base_dir / "part2" / f"Rachel_Isekai_Chapter{i}_HUMANIZED.md")
    
    # Part 3: Chapters 29-43
    for i in range(29, 44):
        chapters.append(base_dir / "part3" / f"Rachel_Isekai_Chapter{i}_HUMANIZED.md")
    
    return chapters

def create_markdown_book(chapters, output_file):
    """Combine all chapters into a single markdown file."""
    print(f"Creating {output_file}...")
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Write title
        outfile.write("# Rachel's Journey\n\n")
        outfile.write("*A Novel*\n\n")
        outfile.write("---\n\n")
        
        for i, chapter_file in enumerate(chapters, 1):
            if not chapter_file.exists():
                print(f"  Warning: {chapter_file.name} not found, skipping...")
                continue
            
            print(f"  Adding {chapter_file.name}...")
            
            with open(chapter_file, 'r', encoding='utf-8') as infile:
                content = infile.read()
                
                # Remove markdown frontmatter if present
                content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
                
                # Write chapter content
                outfile.write(content)
                outfile.write("\n\n")
                
                # Add page break between chapters
                if i < len(chapters):
                    outfile.write("---\n\n")
    
    print(f"[OK] Created {output_file}")

def create_epub_book(chapters, output_file):
    """Create an EPUB from all chapters."""
    print(f"\nCreating {output_file}...")
    
    # Create EPUB book
    book = epub.EpubBook()
    
    # Set metadata
    book.set_identifier('rachel-isekai-full-001')
    book.set_title("Rachel's Journey")
    book.set_language('en')
    book.add_author('Your Name')
    
    # Create chapters and add to book
    epub_chapters = []
    spine = ['nav']
    
    for i, chapter_file in enumerate(chapters, 1):
        if not chapter_file.exists():
            print(f"  Warning: {chapter_file.name} not found, skipping...")
            continue
        
        print(f"  Adding {chapter_file.name}...")
        
        with open(chapter_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove markdown frontmatter if present
        content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
        
        # Convert markdown to HTML
        html_content = markdown.markdown(content)
        
        # Create chapter
        epub_chapter = epub.EpubHtml(
            title=f'Chapter {i}',
            file_name=f'chapter_{i:02d}.xhtml',
            lang='en'
        )
        epub_chapter.content = f'<h1>Chapter {i}</h1>{html_content}'
        
        # Add chapter to book
        book.add_item(epub_chapter)
        epub_chapters.append(epub_chapter)
        spine.append(epub_chapter)
    
    # Add default NCX and Nav files
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    
    # Define Table of Contents
    book.toc = tuple(epub_chapters)
    
    # Define spine
    book.spine = spine
    
    # Write EPUB file
    epub.write_epub(output_file, book, {})
    print(f"[OK] Created {output_file}")

def main():
    """Main function."""
    base_dir = Path(__file__).parent
    
    # Get all chapter files
    chapters = get_chapter_files()
    
    print(f"Found {len(chapters)} chapters to combine\n")
    
    # Create markdown book
    md_output = base_dir / "full_book.md"
    create_markdown_book(chapters, md_output)
    
    # Create EPUB book
    epub_output = base_dir / "full_book.epub"
    create_epub_book(chapters, epub_output)
    
    print("\n[OK] All done!")
    print(f"\nCreated files:")
    print(f"  - {md_output}")
    print(f"  - {epub_output}")

if __name__ == '__main__':
    main()

