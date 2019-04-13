n = int(input())

myList = []
myS = ''
for _ in range(0,n):
	myCommand = input()
	if 'insert' in myCommand:
		nums = myCommand.split()[1:]
		myList.insert(int(nums[0]), int(nums[1]))
	elif 'print' in myCommand:
		print(myList)
	elif 'remove' in myCommand:
		


