import random
import datetime

def bubbleSort(iList):
	iterations = len(iList)
	while (iterations!= 0):
		for count in range(len(iList)):
			if (count < len(iList)-1):
				if (iList[count] > iList[count+1]):
					(iList[count], iList[count+1]) = (iList[count+1],iList[count])
			else:
				continue
		iterations -= 1
	return iList

test = random.sample(xrange(10000), 100)
start = datetime.datetime.now()
test = bubbleSort(test)
end = datetime.datetime.now()
time = end-start
print 'Your list was bubble sorted in:', time
#print time.hour, 'hour(s) |', time.minute, 'minute(s) |', time.second, 'second(s) |', time.microsecond, 'microsecond(s)'
print '\n\nSorted List Now\n\n'
print test
