#!/usr/bin/env python3
"""
Verify no duplicates in words.txt by checking line by line
"""

def verify_no_duplicates(filename):
    """Check each line in the file for duplicates"""
    print(f"Checking {filename} line by line for duplicates...\n")

    words_seen = set()
    duplicates = []
    line_count = 0

    with open(filename, 'r') as f:
        for line_num, line in enumerate(f, 1):
            word = line.strip()
            line_count += 1

            if word in words_seen:
                duplicates.append((line_num, word))
                print(f"✗ Duplicate found at line {line_num}: '{word}'")
            else:
                words_seen.add(word)

            # Progress indicator every 10000 lines
            if line_num % 10000 == 0:
                print(f"  Checked {line_num} lines...")

    print(f"\n{'='*60}")
    print(f"Verification Complete:")
    print(f"{'='*60}")
    print(f"Total lines checked: {line_count}")
    print(f"Unique words found: {len(words_seen)}")
    print(f"Duplicates found: {len(duplicates)}")

    if len(duplicates) == 0:
        print(f"\n✓✓✓ SUCCESS: No duplicates detected! ✓✓✓")
        print(f"All {line_count} words are unique.")
    else:
        print(f"\n✗✗✗ WARNING: {len(duplicates)} duplicate(s) detected ✗✗✗")
        print("\nDuplicate details:")
        for line_num, word in duplicates:
            print(f"  Line {line_num}: '{word}'")

    return len(duplicates) == 0

if __name__ == "__main__":
    success = verify_no_duplicates("words.txt")
    exit(0 if success else 1)
