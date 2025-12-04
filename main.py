import sys

from stats import count_characters, get_num_words, sort_list


def main():
    print(sys.argv)
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        num_words = get_num_words(sys.argv[1])
        num_characters = count_characters(sys.argv[1])
        char_list = sort_list(sys.argv[1])
        print(char_list)
        print(num_characters)

        report_header = """========== BOOKBOT ==========
        Analyzing book found at books/frankenstein.txt...
        ---------- Word Count -------"""
        print(report_header)
        print(f"Found {num_words} total words")
        print("---------- Character Count ---------")
        for val in char_list:
            if val["char"].isalpha():
                print(val["char"] + ": " + str(val["num"]))


main()
