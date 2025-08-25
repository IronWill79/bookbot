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
