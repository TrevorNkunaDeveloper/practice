def is_palindrome(text):
    """
    Function that takes in a string, return True if the string reads the same forward and backward, otherwise False.

    Args: (string): string text input.
    Return: (bool): True, False.
    
    Example:
    is_palindrome("mom")
    >>> True.
    """
    if (text == "".join(reversed(text))):
        return True
    
    return False

print(is_palindrome("mom"))