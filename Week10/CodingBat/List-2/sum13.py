def sum13(nums):
    
    total = 0
    i = 0

    while i < len(nums):
        if nums[i] == 13:
            i += 2
            continue
        total += nums[i]
        i += 1

    return total