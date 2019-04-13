line = input()
subLine = input()

for i in range(0, len(line) - len(subLine)):
	if line[i:len(subLine)+i] == subLine:
		print(i)
		break
	
