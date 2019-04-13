def same_first_last(nums):
    if((len(nums)>=1) and (nums[0]==nums[len(nums)-1])):
        return True
    return False

print(same_first_last([1, 2, 3, 1]))