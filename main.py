import sys
from stats import get_nr_of_words, count_each_character, sort_characters
def get_book_text(path):
    with open(path) as f:
        return f.read()
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_nr_of_words(text)
    chars_dict = count_each_character(text)
    chars_sorted_list = sort_characters(chars_dict)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")

    for item in chars_sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']} times")

    print("--- End report ---")

main()