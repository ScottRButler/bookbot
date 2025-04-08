def get_num_words(text):
    """
    Counts the number of words in a string.

    Args:
        text: The input string.

    Returns:
        The number of words in the string (integer).
    """
    words = text.split()  # Split the string into a list of words using whitespace as the delimiter
    return len(words)


def get_char_count(text):
    """
    Counts the number of times each character (lowercase) appears in a string.

    Args:
        text: The input string.

    Returns:
        A dictionary where keys are lowercase characters (strings) and values are their counts (integers).
    """
    char_counts = {}
    for char in text.lower():  # Convert to lowercase and iterate
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


def sort_char_counts(char_counts):
    """
    Sorts a dictionary of character counts into a list of dictionaries, sorted by count in descending order.

    Args:
        char_counts: A dictionary where keys are characters (strings) and values are their counts (integers).

    Returns:
        A list of dictionaries, where each dictionary has "char" and "count" keys.
        The list is sorted by "count" in descending order.
    """
    sorted_chars = []
    for char, count in char_counts.items():
        if char.isalpha():  # Filter out non-alphabetical characters
            sorted_chars.append({"char": char, "count": count})

    sorted_chars.sort(key=lambda x: x["count"], reverse=True)  # Sort by count, greatest to least
    return sorted_chars