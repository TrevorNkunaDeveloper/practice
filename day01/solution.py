def swap_values(value1, value2):
    """
    Function to that takes in 2 values, returns the values swapped.

    Args: 
        value1: (??(int),(string), ...) first value input.
        value2: (??(int),(string), ...) second value input.

    return: 
        swapped_values: [array] swapped values
    """
    original_values = [value1, value2]

    return [original_values[1],original_values[0]]



print(swap_values("5",3))