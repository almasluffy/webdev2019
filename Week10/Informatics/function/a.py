def mini(a,b,c,d):
	if a<b:
		x1 = a
	else:
		x1 = b
	if c < d:
		x2 = c
	else:
		x2 = d
	if x1<x2:
		return x1
	return x2


nums = [int(x) for x in input().split()]

print(mini(nums[0], nums[1], nums[2],nums[3]))



