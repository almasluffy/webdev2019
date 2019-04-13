def myPow(x,r):
	j = 0
	res = 1

	if r==0 and x!=0:
		return 1
	while j!=r:
		res*=x

		j+=1
	return res


nums = [float(x) for x in input().split()]

print(myPow(nums[0], nums[1]))