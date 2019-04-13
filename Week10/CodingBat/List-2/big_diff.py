def big_diff(nums):
    max = nums[0]
    min = nums[0]
    for i in range(len(nums)):
        if(nums[i] > max):
            max = nums[i]
        elif(nums[i] < min):
        min = nums[i]
    return (max-min)
