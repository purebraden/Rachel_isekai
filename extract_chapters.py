import re

# Read the recovered full book
with open('full_book_RECOVERED.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Split by chapter headers
chapters = re.split(r'\n(?=## Chapter )', content)

# Skip the title/intro section (first split)
chapters = [ch for ch in chapters if ch.startswith('## Chapter')]

print(f"Found {len(chapters)} chapters\n")

# Map chapter numbers to files
chapter_mapping = {
    # Part 1 (1-14)
    1: 'part1/Rachel_Isekai_Chapter1_PATCHED-2.md',
    2: 'part1/Rachel_Isekai_Chapter2_PATCHED-2.md',
    3: 'part1/Rachel_Isekai_Chapter3_ASCII-2.md',
    4: 'part1/Rachel_Isekai_Chapter4_FINAL-2.md',
    5: 'part1/Rachel_Isekai_Chapter5_FINAL-2.md',
    6: 'part1/Rachel_Isekai_Chapter6_REVISED-2.md',
    7: 'part1/Rachel_Isekai_Chapter7_FINAL-2.md',
    8: 'part1/Rachel_Isekai_Chapter8_HUMANIZED.md',
    9: 'part1/Rachel_Isekai_Chapter9_HUMANIZED.md',
    10: 'part1/Rachel_Isekai_Chapter10_HUMANIZED.md',
    11: 'part1/Rachel_Isekai_Chapter11_HUMANIZED.md',
    12: 'part1/Rachel_Isekai_Chapter12_HUMANIZED.md',
    13: 'part1/Rachel_Isekai_Chapter13_HUMANIZED.md',
    14: 'part1/Rachel_Isekai_Chapter14_HUMANIZED.md',
    # Part 2 (16-29, note the gap at 15)
    16: 'part2/Rachel_Isekai_Chapter16_HUMANIZED.md',
    17: 'part2/Rachel_Isekai_Chapter17_HUMANIZED.md',
    18: 'part2/Rachel_Isekai_Chapter18_HUMANIZED.md',
    19: 'part2/Rachel_Isekai_Chapter19_HUMANIZED.md',
    20: 'part2/Rachel_Isekai_Chapter20_HUMANIZED.md',
    21: 'part2/Rachel_Isekai_Chapter21_HUMANIZED.md',
    22: 'part2/Rachel_Isekai_Chapter22_HUMANIZED.md',
    23: 'part2/Rachel_Isekai_Chapter23_HUMANIZED.md',
    24: 'part2/Rachel_Isekai_Chapter24_HUMANIZED.md',
    25: 'part2/Rachel_Isekai_Chapter25_HUMANIZED.md',
    26: 'part2/Rachel_Isekai_Chapter26_HUMANIZED.md',
    27: 'part2/Rachel_Isekai_Chapter27_HUMANIZED.md',
    28: 'part2/Rachel_Isekai_Chapter28_HUMANIZED.md',
    29: 'part2/Rachel_Isekai_Chapter29_HUMANIZED.md',
    # Part 3 (30-43)
    30: 'part3/Rachel_Isekai_Chapter30_HUMANIZED.md',
    31: 'part3/Rachel_Isekai_Chapter31_HUMANIZED.md',
    32: 'part3/Rachel_Isekai_Chapter32_HUMANIZED.md',
    33: 'part3/Rachel_Isekai_Chapter33_HUMANIZED.md',
    34: 'part3/Rachel_Isekai_Chapter34_HUMANIZED.md',
    35: 'part3/Rachel_Isekai_Chapter35_HUMANIZED.md',
    36: 'part3/Rachel_Isekai_Chapter36_HUMANIZED.md',
    37: 'part3/Rachel_Isekai_Chapter37_HUMANIZED.md',
    38: 'part3/Rachel_Isekai_Chapter38_HUMANIZED.md',
    39: 'part3/Rachel_Isekai_Chapter39_HUMANIZED.md',
    40: 'part3/Rachel_Isekai_Chapter40_HUMANIZED.md',
    41: 'part3/Rachel_Isekai_Chapter41_HUMANIZED.md',
    42: 'part3/Rachel_Isekai_Chapter42_HUMANIZED.md',
    43: 'part3/Rachel_Isekai_Chapter43_HUMANIZED.md',
}

# Extract and save each chapter
for i, chapter_content in enumerate(chapters, 1):
    if i == 15:
        print(f"Skipping chapter 15 (gap in numbering)")
        continue
    
    # Adjust for the gap
    chapter_num = i if i < 15 else i + 1
    
    if chapter_num in chapter_mapping:
        filename = chapter_mapping[chapter_num]
        
        # Clean up the chapter content
        chapter_content = chapter_content.strip()
        
        # Write to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(chapter_content + '\n\n')
        
        print(f"Extracted Chapter {chapter_num} -> {filename}")
    else:
        print(f"WARNING: No mapping for chapter {chapter_num}")

print("\n[OK] All chapters extracted!")

