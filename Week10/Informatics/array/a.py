# n = int(input())
# digits = []
# for x in range(0,6):
# 	a = int(input())
#     digits[x]=a

# for x in range(0,6):
# 	print(digits[x])

# digits = [input() for x in range(5)]

# print(digits)

m = int(input())

arr=[a for a in input().split()][:m]


for x in range(0,m):
	if(x%2==0):
		print(arr[x],end=' ')
	
