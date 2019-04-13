n = int(input())

Data = {}

for _ in range(0,n):
	line = input().split()

	Data[line[0]] = sum([float(x) for x in line[1:]])/3

ourName = input()

print(Data[ourName])


