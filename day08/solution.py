def max_of_two(a,b):
    """
    Return the maximum of two numbers.
    Args: (int): a, b.
    Return: (int): maximum of a and b.
    
    Example:
    max_of_two(3, 5)
    >>> 5.
    """
    if( a > b):
        return a
    elif( a < b):
        return b
    else:
        return a
    
print(max_of_two(6, 6))