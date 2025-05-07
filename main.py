import sys
from stats import count_words, count_characters, sort_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main(book):
    book_text = get_book_text(book)
    book_characters = count_characters(book_text)
    sorted_characters = sort_dictionary(book_characters)
    character_count_string = ""
    for dict in sorted_characters:
        if dict["char"].isalpha():
            character_count_string += dict["char"] + ": " + str(dict["num"]) + "\n"
        if sorted_characters.index(dict) == len(sorted_characters) - 1:
            character_count_string = character_count_string[:-1]
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book}...\n----------- Word Count ----------\nFound {count_words(book_text)} total words\n--------- Character Count -------\n{character_count_string}\n============= END ===============")

try:
    main(sys.argv[1])
except IndexError:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
