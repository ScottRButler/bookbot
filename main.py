import sys
from stats import get_num_words, get_char_count, sort_char_counts  # Import the functions

def get_book_text(filepath):
    """
    Reads the contents of a file and returns it as a string.

    Args:
        filepath: The path to the file (string).

    Returns:
        The entire content of the file as a string.  Returns an empty string if the file
        cannot be opened.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:  # Explicitly specify UTF-8 encoding
            text = file.read()
            return text
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}") # more general exception capture
        return ""




def main():
    """
    Reads the content of a book file (path provided as command-line argument),
    counts the words and characters, and prints the formatted report.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with a non-zero status code to indicate an error

    filepath = sys.argv[1]  # Get the filepath from the command-line argument

    book_text = get_book_text(filepath)

    if book_text:
        num_words = get_num_words(book_text)
        char_counts = get_char_count(book_text)
        sorted_char_counts = sort_char_counts(char_counts)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        for char_info in sorted_char_counts:
            print(f"{char_info['char']}: {char_info['count']}")

        print("============= END ==============")


if __name__ == "__main__":
    main()