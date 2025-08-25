def count_words(text):
    return len(text.split())


def count_chars(text):
    char_counts = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
