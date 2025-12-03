from stats import count_characters, get_num_words, sort_list


def main():
    num_words = get_num_words()
    num_characters = count_characters()
    char_list = sort_list()
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
