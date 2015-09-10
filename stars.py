import sys

def printStars(iNum):
	for count in range(iNum):
		sys.stdout.write('*')
	print ''

def printAlphas(iStr):
	for count in range(len(iStr)):
		sys.stdout.write(iStr[0].lower())
	print ''

def stars(iList):
	for element in iList:
		if isinstance(element, str):
			printAlphas(element)
		elif isinstance(element, int):
			printStars(element)



test = [1, 2, 6, 4, 3, 6, 8, 4]
stars(test)
raw_input('\n\nPress Enter to continue to part 2....\n\n')
test2 =[4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
stars(test2)
raw_input('\n\nPress Enter to end....\n\n')


