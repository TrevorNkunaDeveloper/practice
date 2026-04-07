def square(num):
    """
    Takes in an integer, then prints a square using # character.

    Args:
        num: positive integer input parameter.

    return:
        void: Prints out # sqaures of the input number.

    Example:
    >>> sqaure(2)
    ##
    ##

    Example:
    >>> sqaure(3)
    ###
    ###
    ###
    """

    for i in range(num):
        for j in range(num):
            print("#", end="")
        print("")

square(7)