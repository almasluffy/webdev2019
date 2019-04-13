a = set()

n = int(input())

mySum = 0

myList = [int(x) for x in input().split()]

for x in myList:
	a.add(x)
for x in a:
	mySum+=x
print(mySum/len(a))