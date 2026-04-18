def binary_search(nums, target):
    nums_s = sorted(nums)
    found = -1

    for i in range(len(nums_s)):
        if nums_s[i] == target:
            print (f"found at {i}")
            found = i
           
    return found
    
print(binary_search([-1, 0, 3, 5, 9, 12], 15))