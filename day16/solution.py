def move_zeroes(nums):
    if not nums or 0 not in nums:
        return nums
    
    for i in range(len(nums)):

        if nums[i] == 0:
            nums.append(0)
            nums.remove(nums[i])
    return nums
            
print(move_zeroes([1,0,2,5,3,1,0]))