m = int(input())

arr=[int(a) for a in input().split()][:m]

reverse_a = arr[::-1]

for i in range(0,m):
	print(reverse_a[i],end=' ')
		