def get_student_mark(records, name):
    """
    Given a dictionary mapping student names to marks, return the student's mark 
    if found, otherwise return 'Not found'.

    Args: (dict): records.
          (string): name.

    Return: (dict). Value of the key input.

    Example:
    get_student_mark({"Trevor":70, "Sara":65},"Sara"):
    >>> 65
    """

    my_dict = {}
    my_dict = records

    return my_dict.get(name,"Not found")



get_student_mark({"Trevor":70, "Sara":65},"Trevor")