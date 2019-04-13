def sum67(nums):
    ok = True
    total = 0

    for n in nums:
        if n == 6:
            ok = False

        if ok:
            total += n
            continue

        if n == 7:
            ok = True

    return total
