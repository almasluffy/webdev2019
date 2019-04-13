import math
a = int(input())

k = 0

while True:
	if math.pow(2,k) >a:
		break
	print(int(math.pow(2,k)), end=' ')
	k+=1;