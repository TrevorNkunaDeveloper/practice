def common_elements(list1,list2):
    """
    Returns a list of unique values that appear in both lists.
    Args: (list): list1, list2.
    Returns: (list): unique_vals_list.
    Example:
        common_elements([1,2,3,4,5],[1,3,5])
        >>> [1,3,5]
    """
    if not list1 or not list2:
        raise ValueError("1 of the lists is empty.")
    
    combined_list = list1 + list2
    result_list = []

    for value in combined_list:
        if value in list1 and value in list2:
            if value not in result_list:
                result_list.append(value)

    return result_list

print(common_elements([1,2,4],[1,2,3]))