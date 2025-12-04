from typing import TypedDict


class CharEntry(TypedDict):
    char: str
    num: int


def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_string = f.read()

    return file_string


def count_words(book_contents: str) -> int:
    return len(book_contents.split())


def count_characters(book_path: str) -> dict[str, int]:
    book_contents = get_book_text(book_path)
    characters: dict[str, int] = {}

    for char in book_contents.lower():
        characters[char] = characters.get(char, 0) + 1

    return characters


def sort_list(book_path: str) -> list[CharEntry]:
    char_arr: list[CharEntry] = []
    char_dict = count_characters(book_path)
    for key, val in char_dict.items():
        entry: CharEntry = {"char": key, "num": val}
        entry["char"] = key
        entry["num"] = val
        char_arr.append(entry)

    def sort_on(chars: CharEntry) -> int:
        return int(chars["num"])

    char_arr.sort(reverse=True, key=sort_on)

    return char_arr


def get_num_words(book_path: str):
    contents = get_book_text(book_path)
    return count_words(contents)
