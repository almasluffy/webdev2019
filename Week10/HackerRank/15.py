
def changeMyString(ourString, index, chr):
	ourString = ourString[:index] + chr + ourString[index+1:]
	return ourString

if __name__ == '__main__':
	ourString = input()
	toChange = [x for x in input().split()]
	ourString = changeMyString(ourString, int(toChange[0]), toChange[1])
	print(ourString)