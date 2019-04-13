def toUpper(s):
	newS = s[0].upper() + s[1:]
	return newS

myLine = [x for x in input().split()]

for i in range(0,len(myLine)):
	myLine[i] = toUpper(myLine[i])


for i in range(0, len(myLine)):
	print(myLine[i],end=' ')