def multiples(max):
    """
    Take in a number, sum all natural numbers that are multples 
    of 3 and 5 that are less that that number.

    Args:
        max(int): number which serves as maxum.

    returns:
        void: but prints ths num of the the natural numbers.
    """


    num1 = 3
    num2 = 5
    total = 0

    for i in range(max):
        if i % num1 == 0 or  i % num2 == 0:
            print(i)
            total+=i

    print(f"Sum is : {total}")


multiples(10)    