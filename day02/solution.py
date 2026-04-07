def even_or_odd(num):
    """
    Function that takes in a number, returns string "even" or "odd".
    
    Args: (int) num.
    returns: (string) even_or_odd.

    Example: 
    even_or_odd(9)
    >>> "odd"
    """
    if (num % 2 == 0):
        return "even"
    else:
        return "odd"

print(even_or_odd(10))