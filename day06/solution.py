def two_sum(num_list,target):
    """
    Given a list of integers and a target value, return the indices of 
    two numbers whose sum equals the target. 
    Args: (list) nums. input integers.
          (int) target. Target value.
    Return: (array) indices of two values.

    Example:
    two_sum([2,5,3,4,7],10)
    >>> [2,4]
    """
    for i in range(len(num_list)):
        for j in range(i+1,len(num_list)):
            if(num_list[i] + num_list[j] == target):
                return [i,j]
            
print(two_sum([3,5,8,9,1,1,1,3],6))