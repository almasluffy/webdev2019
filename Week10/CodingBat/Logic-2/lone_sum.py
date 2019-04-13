def lone_sum(a, b, c):
  nums = (a, b, c)
  return sum(n for n in nums if nums.count(n) == 1)