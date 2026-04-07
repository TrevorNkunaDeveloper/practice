def has_three(num1,num2):
    """
    Function to check is 2 numbers = 3 or sum has 3.

    Args:
        num1 (int): first positive number.
        num2 (int): Second Positive number.

        returns:
            bool: True if one of the numbers is 3, or is the sum contains '3',
            otherwise False.

        Example:
            >>> has_three(3,30)
            True
            >>> has_three(3,5)
            False
    
    """
    if (num1 == 3 or num2 == 3) and str(3) in str(num1+num2) :
        return True
    else:
        return False
    
    
print(has_three(3,30))

