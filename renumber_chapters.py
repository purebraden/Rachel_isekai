import os
import re

# Mapping of old chapter numbers to new chapter numbers
# Part 2: 16→15, 17→16, 18→17, 19→18, 20→19, 21→20, 22→21, 23→22, 24→23, 25→24, 26→25, 27→26, 28→27, 29→28
# Part 3: 30→29, 31→30, ... 43→42

def get_chapter_word(num):
    """Convert chapter number to word form"""
    words = {
        1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
        6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
        11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
        16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty",
        21: "Twenty-One", 22: "Twenty-Two", 23: "Twenty-Three", 24: "Twenty-Four", 25: "Twenty-Five",
        26: "Twenty-Six", 27: "Twenty-Seven", 28: "Twenty-Eight", 29: "Twenty-Nine", 30: "Thirty",
        31: "Thirty-One", 32: "Thirty-Two", 33: "Thirty-Three", 34: "Thirty-Four", 35: "Thirty-Five",
        36: "Thirty-Six", 37: "Thirty-Seven", 38: "Thirty-Eight", 39: "Thirty-Nine", 40: "Forty",
        41: "Forty-One", 42: "Forty-Two", 43: "Forty-Three"
    }
    return words[num]

# Process files in reverse order to avoid conflicts
chapters_to_rename = []

# Update Chapter 15 header (file already renamed from 16→15)
if os.path.exists("part2/Rachel_Isekai_Chapter15_HUMANIZED.md"):
    chapters_to_rename.append(("part2/Rachel_Isekai_Chapter15_HUMANIZED.md", "part2/Rachel_Isekai_Chapter15_HUMANIZED.md", 16, 15))

# Part 2: 17-29 → 16-28
for old_num in range(17, 30):
    new_num = old_num - 1
    old_file = f"part2/Rachel_Isekai_Chapter{old_num}_HUMANIZED.md"
    new_file = f"part2/Rachel_Isekai_Chapter{new_num}_HUMANIZED.md"
    if os.path.exists(old_file):
        chapters_to_rename.append((old_file, new_file, old_num, new_num))

# Part 3: 30-43 → 29-42
for old_num in range(30, 44):
    new_num = old_num - 1
    old_file = f"part3/Rachel_Isekai_Chapter{old_num}_HUMANIZED.md"
    new_file = f"part3/Rachel_Isekai_Chapter{new_num}_HUMANIZED.md"
    if os.path.exists(old_file):
        chapters_to_rename.append((old_file, new_file, old_num, new_num))

# Process in reverse order
chapters_to_rename.reverse()

print(f"Renumbering {len(chapters_to_rename)} chapters...\n")

for old_path, new_path, old_num, new_num in chapters_to_rename:
    # Read the file
    with open(old_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update chapter header
    old_word = get_chapter_word(old_num)
    new_word = get_chapter_word(new_num)
    
    # Replace the chapter header
    content = re.sub(
        f"^## Chapter {old_word}$",
        f"## Chapter {new_word}",
        content,
        flags=re.MULTILINE
    )
    
    # Write to new filename
    with open(new_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  Renamed: {os.path.basename(old_path)} -> {os.path.basename(new_path)}")
    print(f"           Updated header: Chapter {old_word} -> Chapter {new_word}")
    
    # Delete old file if different from new
    if old_path != new_path:
        os.remove(old_path)

print("\n[OK] All chapters renumbered!")
print("\nChapter sequence is now: 1-42 (no gaps)")

