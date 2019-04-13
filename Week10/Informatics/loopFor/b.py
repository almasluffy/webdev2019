a = int(input())
b = int(input())
c = int(input())
d = int(input())

for x in range(a,b+1):
	if x%d==c:
		print(x,end=' ')
