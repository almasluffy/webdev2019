m = int(input())

arr=[int(a) for a in input().split()][:m]

k = 0
for x in range(1,m-1):
	if arr[x] > arr[x-1] and arr[x] > arr[x+1]:
		k+=1

print(k)

	
		