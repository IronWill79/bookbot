from typing import TypedDict

def count_words(text: str) -> int:
    return len(text.split())


def count_chars(text: str) -> dict[str, int]:
    char_counts: dict[str, int] = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


CharCount = TypedDict('CharCount', {'char': str, 'num': int})

def sort_on_counts(char_counts: CharCount) -> int:
    return char_counts["num"]


def get_sorted_char_counts(char_counts: dict[str, int]) -> list[CharCount]:
    char_count_list: list[CharCount] = []
    for char in char_counts:
        char_count_list.append({"char": char, "num": char_counts[char]})
    char_count_list.sort(reverse=True, key=sort_on_counts)
    return char_count_list
