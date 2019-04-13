def no_teen_sum(a, b, c):
    nums = (a, b, c)
    return sum(fix_teen(n) for n in nums)


def fix_teen(n):
  if(n < 13 or n > 19 or n == 15 or n == 16):
    return n
  return 0