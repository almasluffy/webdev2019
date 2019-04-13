m = int(input())

arr=[int(a) for a in input().split()][:m]


for x in range(0,m):
	if(arr[x]%2==0):
		print(arr[x],end=' ')