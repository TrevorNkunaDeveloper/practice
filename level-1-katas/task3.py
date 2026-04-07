def is_sixty_five(num1, num2):
    """
    Takes in 2 numbers. If either of the numbers is 65 or the sum is 65,
      it returns True, otherwise False.

      Args:
      num1 (int) : first positive integer.
      num2 (int) : second positive integer.

      Returns:
        Bool: True is one of the numbers or the sum is 65, otherwise False.

      Example:
      >>> is_sixty_five(2,9)
      False
      >>> is_sixty_five(65,0)
      True
    """

    if (num1 == 65 or num2 == 65) or (num1 + num2) == 65 :
        return True
    else:
        return False 
    


print(is_sixty_five(65,0))