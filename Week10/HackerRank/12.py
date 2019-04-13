
def swap_case(myString):
	res = ''

	for myChar in myString:
		if myChar.islower():
			res+=myChar.upper()
		else:
			res+=myChar.lower()
	return res
	
line = input()
print(swap_case(line))



