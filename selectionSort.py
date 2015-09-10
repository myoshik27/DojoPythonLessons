import random
import datetime

def selectionSort(iList):
	iterations = len(iList)
	lownum = iList[0]
	lownumindex = 0
	indexcounter = 0
	
	while (indexcounter != iterations-1):
		# print 'while loop # ', indexcounter
		# print 'lownum:', lownum
		# print 'lownumindex:', lownumindex
		# print 'indexcounter:', indexcounter
		# print 'iterations:', iterations
		print 'The List is now:', iList, '\n'
		for count in range(indexcounter, iterations):
			if (iList[count] < lownum):
				# print 'low number found at index:', count, ' and its value is', iList[count]
				lownum = iList[count]
				lownumindex = count
				# print 'After update lownum:', lownum, 'and lownumindex:', lownumindex, '\n'
		(iList[indexcounter],iList[lownumindex]) = (iList[lownumindex],iList[indexcounter])
		indexcounter += 1
		lownum = iList[indexcounter]
		lownumindex = indexcounter
	return iList
	# #index = 0
	# #iterations = len(iList) - 1
	# while (index != iterations):
	# 	for count in range(len(iList) - index):
	# 		if (iList[count] < lownum):
	# 			lownum = iList[count]
	# 			iList[index] = lownum
	# 		else:
	# 			continue
	# 	index += 1
	# return iList
test = random.sample(xrange(20), 10)
print test
#test = random.sample(xrange(10000), 100)
start = datetime.datetime.now()
test = selectionSort(test)
end = datetime.datetime.now()
time = end-start
print 'Your list was slection sorted in:', time
#print time.hour, 'hour(s) |', time.minute, 'minute(s) |', time.second, 'second(s) |', time.microsecond, 'microsecond(s)'
print '\n\nSorted List Now\n\n'
print test