import math
a = int(input())
k = 0
res = 0
while True:
	if math.pow(2,k)>a:
		break;
	if math.pow(2,k)==a:
		res+=1
	k+=1
if res==0:
	print("NO")
if res!=0:
	print("YES")