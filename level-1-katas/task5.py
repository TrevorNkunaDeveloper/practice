import math 
def triangle(num):
    """
    Take in an integer, print a triangle accordinly.

    Args:
        num (int): positive, or negative number input.

    Return: 
        void: Prints "#" in triangle format

    Example:
        >>> triangle(3)
        #
        ##
        ###

        >>> triangle(-3)
        ####
        ##
        #
    """
    if(num >= 0):
        for i in range(num):
            for j in range(i+1):
                print("#", end="")
            print("")
    else:
        for i in range(int(math.fabs(num))+1,0,-1):
            for j in range(i-1):
                print("#", end="")
                
            print("")    


triangle(-5)