a = int(input())
b = int(input())

for x in range(1, int( (b)**0.5)+1):
	if x*x >= a:
		print(x*x, end=' ')
	else:
		print('',end=' ')