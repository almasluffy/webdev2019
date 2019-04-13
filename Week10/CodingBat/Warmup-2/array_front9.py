def array_front9(nums):
    e = len(nums)
    if e > 4:
        e = 4
  
    for i in range(e):
        if nums[i] == 9:
            return True
        return False