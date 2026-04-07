def find_max(numbers_list):
    """
    Function to take in an array of numbers, reads the array from beging to finish, and returns the largest.
    Args: (array) numbers, an array of numbers.
    Returns: (int) largest number.

    Example:
    find_max([3,6,5,9,4])
    >>> 9
    """
    if (not numbers_list):
        print()
        raise ValueError("Array empty")
    else:
        largest_value = int(numbers_list[0])

        for i in range(len(numbers_list)):
            if numbers_list[i] > largest_value:
                largest_value = numbers_list[i]

    return largest_value


print(find_max([3,8,2,10,4]))