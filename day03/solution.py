def sum_to_n(number):
    """
    Function to return the sum of all integers from 1 up to n. Return 0 for non-positive numbers.

    Args: (int) input number.
    Reurn: (int) Sum to n.

    Example:
    sum_to_n(5)
    >>> 15
    """
    count = 0
    if (number*1 == -number):
        return 0

    for i in range(number+1):
        count+=i

    return count
    


print(sum_to_n(4))