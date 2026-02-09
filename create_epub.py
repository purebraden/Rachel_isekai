#!/usr/bin/env python3
"""
Create an EPUB file from Rachel Isekai chapters
"""
import os
import zipfile
from pathlib import Path
import re

def markdown_to_html(markdown_text):
    """Convert basic markdown to HTML"""
    html = markdown_text
    
    # Convert headers
    html = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    
    # Convert paragraphs (lines separated by blank lines)
    paragraphs = []
    current_para = []
    
    for line in html.split('\n'):
        line = line.strip()
        if line.startswith('<h'):
            if current_para:
                paragraphs.append('<p>' + ' '.join(current_para) + '</p>')
                current_para = []
            paragraphs.append(line)
        elif line:
            current_para.append(line)
        elif current_para:
            paragraphs.append('<p>' + ' '.join(current_para) + '</p>')
            current_para = []
    
    if current_para:
        paragraphs.append('<p>' + ' '.join(current_para) + '</p>')
    
    return '\n'.join(paragraphs)

def create_epub(chapters_dir, output_file):
    """Create an EPUB file from markdown chapters"""
    
    # Chapter files in order
    chapter_files = [
        'Rachel_Isekai_Chapter1_PATCHED-2.md',
        'Rachel_Isekai_Chapter2_PATCHED-2.md',
        'Rachel_Isekai_Chapter3_ASCII-2.md',
        'Rachel_Isekai_Chapter4_FINAL-2.md',
        'Rachel_Isekai_Chapter5_FINAL-2.md',
        'Rachel_Isekai_Chapter6_REVISED-2.md',
        'Rachel_Isekai_Chapter7_FINAL-2.md',
        'Rachel_Isekai_Chapter8_FINAL-2.md',
        'Rachel_Isekai_Chapter9_HUMANIZED.md',
        'Rachel_Isekai_Chapter10_HUMANIZED.md',
        'Rachel_Isekai_Chapter11_HUMANIZED.md',
        'Rachel_Isekai_Chapter12_HUMANIZED.md',
        'Rachel_Isekai_Chapter13_HUMANIZED.md',
        'Rachel_Isekai_Chapter14_HUMANIZED.md',
    ]
    
    # Create EPUB (which is a ZIP file)
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as epub:
        # Add mimetype (must be first and uncompressed)
        epub.writestr('mimetype', 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
        
        # Add container.xml
        container_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
    <rootfiles>
        <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
    </rootfiles>
</container>'''
        epub.writestr('META-INF/container.xml', container_xml)
        
        # Read all chapters
        chapters_html = []
        for i, chapter_file in enumerate(chapter_files, 1):
            chapter_path = os.path.join(chapters_dir, chapter_file)
            with open(chapter_path, 'r', encoding='utf-8') as f:
                markdown = f.read()
                html_content = markdown_to_html(markdown)
                
                # Create full HTML page
                full_html = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Chapter {i}</title>
    <style>
        body {{ font-family: Georgia, serif; line-height: 1.6; margin: 2em; }}
        h1, h2, h3 {{ font-family: Arial, sans-serif; }}
        h1 {{ font-size: 2em; margin-top: 1em; }}
        h2 {{ font-size: 1.5em; margin-top: 0.8em; }}
        p {{ margin: 1em 0; text-align: justify; }}
    </style>
</head>
<body>
{html_content}
</body>
</html>'''
                
                epub.writestr(f'OEBPS/chapter{i}.xhtml', full_html)
                chapters_html.append(i)
        
        # Create content.opf
        manifest_items = '\n'.join([
            f'    <item id="chapter{i}" href="chapter{i}.xhtml" media-type="application/xhtml+xml"/>'
            for i in chapters_html
        ])
        
        spine_items = '\n'.join([
            f'    <itemref idref="chapter{i}"/>'
            for i in chapters_html
        ])
        
        content_opf = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="BookID">
    <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
        <dc:title>Rachel's Isekai Journey</dc:title>
        <dc:creator>Author</dc:creator>
        <dc:language>en</dc:language>
        <dc:identifier id="BookID">rachel-isekai-part1</dc:identifier>
        <meta property="dcterms:modified">2026-02-09T00:00:00Z</meta>
    </metadata>
    <manifest>
        <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
{manifest_items}
    </manifest>
    <spine toc="ncx">
{spine_items}
    </spine>
</package>'''
        epub.writestr('OEBPS/content.opf', content_opf)
        
        # Create toc.ncx
        nav_points = '\n'.join([
            f'''    <navPoint id="chapter{i}" playOrder="{i}">
        <navLabel><text>Chapter {i}</text></navLabel>
        <content src="chapter{i}.xhtml"/>
    </navPoint>'''
            for i in chapters_html
        ])
        
        toc_ncx = f'''<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
    <head>
        <meta name="dtb:uid" content="rachel-isekai-part1"/>
        <meta name="dtb:depth" content="1"/>
    </head>
    <docTitle>
        <text>Rachel's Isekai Journey</text>
    </docTitle>
    <navMap>
{nav_points}
    </navMap>
</ncx>'''
        epub.writestr('OEBPS/toc.ncx', toc_ncx)
    
    print(f"[SUCCESS] EPUB created: {output_file}")
    print(f"[SUCCESS] Included {len(chapter_files)} chapters")

if __name__ == '__main__':
    chapters_dir = r'C:\Dev\Rachel_isekai\part1'
    output_file = r'C:\Dev\Rachel_isekai\Rachel_Isekai_Part1.epub'
    
    create_epub(chapters_dir, output_file)
    print(f"\nYou can now transfer this file to your iPhone and open it with Apple Books!")

