D = {}
myMin2 = -1

N = int(input())
for _ in range(0,N):
	name = input()
	score = float(input())
	D[name] = score

mini = min(D.values())

for el in sorted(D.values()):
	if el !=mini:
		M = el
		break
for x in sorted(D):
    if D[x] == M:
    	print(x)



