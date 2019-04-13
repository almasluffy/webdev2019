m = int(input())

arr=[int(a) for a in input().split()][:m]

k = 0;
for x in range(0,m):
	if(arr[x]>0):
		k+=1;

print(k)
		