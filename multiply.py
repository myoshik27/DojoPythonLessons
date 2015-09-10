def mulitply(iList):
	#setup and test counter
	count = 0
	print 'Count is:', count

	#start loop to do math
	for numbers in iList:
		print numbers, 'is now', numbers * 5
		iList[count] = numbers * 5
		print iList[count]
		count += 1
		print 'Count is:', count
	#return list
	return iList

#main program

a = [10, 20, 30, 40, 50]
print 'List was:', a
#call function
a = mulitply(a)
#output to screen
print 'List now:', a