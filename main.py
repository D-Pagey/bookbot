import sys
from stats import get_word_count, count_characters, sorted_counts

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    args = sys.argv

    if len(args) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    filepath = args[1]
    contents = get_book_text(filepath)
    word_count = get_word_count(contents)
    counts = count_characters(contents)
    sorted = sorted_counts(counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


    

main()
