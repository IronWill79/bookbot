from stats import count_chars, count_words, get_sorted_char_counts

def main() -> None:
    print_report_of_file("books/frankenstein.txt")


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def print_report_of_file(filepath: str) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    text = get_book_text(filepath)
    word_count = count_words(text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_counts = get_sorted_char_counts(count_chars(text))
    for char in char_counts:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")


main()
