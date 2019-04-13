line = input()
myWidth = int(input())

iNeed = len(line) % myWidth;
k = 0
for i in range(0, int(len(line)/myWidth)):
	if k == 0:
		print(line[i:myWidth+i])
	else:
		print(line[i*myWidth: i*myWidth+myWidth])
	k+=1;
if len(line)%myWidth!=0:
		print(line[-iNeed:])


