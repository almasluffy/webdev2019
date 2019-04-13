n = int(input())

arr = [int(x) for x in input().split()];


arr = sorted(arr,reverse=True)

maxN = max(arr)


for x in arr:
	if x != maxN:
		print(x)
		break