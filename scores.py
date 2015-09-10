iList = []
for count in range(0,10):
	iList.append(input('Enter student score:'))
	if iList[count] >= 60 and iList[count] <= 100:
		continue
	else:
		print 'Score must be in the 60-100 range'
		iList[count] = input('Enter student score:')

print 'Scores and Grades'
for count in range(0,10):
	if iList[count] >= 60 and iList[count] <= 69:
		print 'Score: '+str(iList[count])+'; Your grade is D'
	elif iList[count] >= 70 and iList[count] <= 79:
		print 'Score: '+str(iList[count])+'; Your grade is C'
	elif iList[count] >= 80 and iList[count] <= 89:
		print 'Score: '+str(iList[count])+'; Your grade is B'
	else:
		print 'Score: '+str(iList[count])+'; Your grade is A'
count += 1