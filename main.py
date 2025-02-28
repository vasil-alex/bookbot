from collections import Counter
from stats import sort
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]

def read():
    with open(book_path) as f:
        story_content = f.read()
    return story_content

def words(story_content):
    words = story_content.split()
    word_count = len(words)
    return word_count

def letters(story_content):

    lowered_string = story_content.lower()
    letter_count = Counter(c for c in lowered_string if c.isalpha())
    return letter_count


def main():

    story_content = read()
    word_count = words(story_content)
    char_dict = letters(story_content)
    sorted_chars = sort(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_info in sorted_chars:
        for char, count in char_info.items():
            if char.isalpha():
                 print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    main()