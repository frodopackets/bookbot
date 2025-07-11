def get_num_words(book_text):
    """
    Counts the number of words in a given text.

    Args:
        book_text: A string containing the text to be analyzed.

    Returns:
        An integer representing the number of words in the text.
    """
    if not book_text:
        return 0
    # Split the text into words and count them
    num_words = book_text.split()
    return len(num_words)

def get_count_unique_chars(book_text):
    """
    Counts the number of times each unique characters occurs in a given text. All upper case characters should be made lowercase.

    Args:
        book_text: A string containing the text to be analyzed.

    Returns:
        A dictionary with unique characters as keys and their counts as values.
    """
    if not book_text:
        return 0
    # Use a dictionary to count occurrences of each character
    char_count = {}
    for char in book_text.lower():
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def sort_list_of_dicts(dictionary):
    """
    Take dictionary of characters and their counts and returns a sorted list of dictionaries. List is sorted from greatest to least by count. Print report to console and skip non-alphabetical characters using isalpha()

    Args:
        list_of_dicts: A list of dictionaries to be sorted.
        key_name: The key in the dictionaries by which to sort.

    Returns:
        A sorted list of dictionaries.
    """
    sorted_list = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    for item in sorted_list:
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")
        else:
            pass
    return sorted_list