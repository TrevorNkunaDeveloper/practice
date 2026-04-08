def count_evens(numbers):
    count = 0

    if not numbers:
        return count
    
    for value in numbers:
        if value % 2 == 0:
            count+=1
    return count
        