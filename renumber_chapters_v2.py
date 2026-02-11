import os
import re
import shutil

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

print("Renumbering chapters (two-pass approach to avoid conflicts)...\n")

# PHASE 1: Rename all files to temporary names
print("Phase 1: Creating temporary files...\n")
temp_files = []

# Part 2: 16-29 -> temp
for old_num in range(16, 30):
    old_file = f"part2/Rachel_Isekai_Chapter{old_num}_HUMANIZED.md"
    temp_file = f"part2/Rachel_Isekai_Chapter{old_num}_TEMP.md"
    if os.path.exists(old_file):
        shutil.copy2(old_file, temp_file)
        temp_files.append((temp_file, old_num, old_num - 1, "part2"))
        print(f"  Copied: {os.path.basename(old_file)} -> {os.path.basename(temp_file)}")

# Part 3: 30-43 -> temp
for old_num in range(30, 44):
    old_file = f"part3/Rachel_Isekai_Chapter{old_num}_HUMANIZED.md"
    temp_file = f"part3/Rachel_Isekai_Chapter{old_num}_TEMP.md"
    if os.path.exists(old_file):
        shutil.copy2(old_file, temp_file)
        temp_files.append((temp_file, old_num, old_num - 1, "part3"))
        print(f"  Copied: {os.path.basename(old_file)} -> {os.path.basename(temp_file)}")

# PHASE 2: Rename temp files to final names with updated headers
print("\nPhase 2: Renaming to final names and updating headers...\n")

for temp_file, old_num, new_num, directory in temp_files:
    # Read the temp file
    with open(temp_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update chapter header
    old_word = get_chapter_word(old_num)
    new_word = get_chapter_word(new_num)
    
    content = re.sub(
        f"^## Chapter {old_word}$",
        f"## Chapter {new_word}",
        content,
        flags=re.MULTILINE
    )
    
    # Write to final filename
    new_file = f"{directory}/Rachel_Isekai_Chapter{new_num}_HUMANIZED.md"
    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  Created: {os.path.basename(new_file)} (Chapter {old_word} -> {new_word})")
    
    # Delete temp file
    os.remove(temp_file)

# PHASE 3: Delete old files
print("\nPhase 3: Removing old numbered files...\n")

for old_num in range(16, 30):
    old_file = f"part2/Rachel_Isekai_Chapter{old_num}_HUMANIZED.md"
    if os.path.exists(old_file):
        os.remove(old_file)
        print(f"  Removed: {os.path.basename(old_file)}")

for old_num in range(30, 44):
    old_file = f"part3/Rachel_Isekai_Chapter{old_num}_HUMANIZED.md"
    if os.path.exists(old_file):
        os.remove(old_file)
        print(f"  Removed: {os.path.basename(old_file)}")

print("\n[OK] All chapters renumbered!")
print("\nChapter sequence is now: 1-42 (no gaps)")
print("  Part 1: Chapters 1-14")
print("  Part 2: Chapters 15-28")
print("  Part 3: Chapters 29-42")

