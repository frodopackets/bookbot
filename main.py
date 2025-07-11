import sys
from stats import get_num_words, get_count_unique_chars, sort_list_of_dicts

def get_book_text(filepath):
  """
  Reads the content of a file and returns it as a string.

  Args:
    filepath: The path to the file.

  Returns:
    A string containing the entire content of the file.
    Returns an empty string if the file cannot be opened or read.
  """
  try:
    with open(filepath, 'r', encoding='utf-8') as file:
      content = file.read()
    return content
  except FileNotFoundError:
    print(f"Error: The file '{filepath}' was not found.")
    return ""
  except Exception as e:
    print(f"An error occurred while reading the file '{filepath}': {e}")
    return ""


def main(book):
  """
  Main function to demonstrate reading a book text.

  Args:
    get_book_text: Function to read the book text.
  """
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  filepath = sys.argv[1]
  book_content = get_book_text(filepath)
  if book_content:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_content)} total words")
    print("--------- Character Count -------")  # Print the entire book text
    sort_list_of_dicts(get_count_unique_chars(book_content))
  else:
    print("Failed to read the book text.")

main(sys.argv)
