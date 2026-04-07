def remove_duplicates(items_list):
    """
    Function that takes in a list, checks all duplicates, removes duplicates, return clean list.
    Args: items_list (list). Input List of items.
    Return: clean_list (list). Returns clean list of items.

    Example:
        remove_duplicates([1,1,2,3,4,4,5,6])
        >>> [1,2,3,4,5,6] 
    """

    clean_list = []

    if not items_list:
        return []

    for i in range(len(items_list)):
        if items_list[i] not in clean_list:
            clean_list.append(items_list[i])

    return clean_list


print(remove_duplicates([1,2,3,4,5,2,3,4,5,6,6,1]))
