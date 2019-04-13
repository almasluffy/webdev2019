m = int(input())

arr=[int(a) for a in input().split()][:m]

k = 0
b = 0
for x in range(0,m):
	if b>0:
		if arr[x] >arr[x-1]:
			k+=1
	b+=1

print(k)
		