def max_end3(nums):
    max_num = nums[0]
    if(nums[0]<nums[2]):
        max_num = nums[2]
    return([max_num,max_num,max_num])