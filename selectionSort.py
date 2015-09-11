import random
import datetime

def selectionSortMax(iList):
    trips = len(iList)/2  
    lownum = iList[0]
    lownumindex = loopcounter = floor = 0 #setting various counters to zero, floor controls loop for min #
    highnum = iList[len(iList)-1]   #sets the last element as the inital high number for check
    highnumindex = len(iList)-1     #sets index of high element to end for swap
    ceiling = len(iList)    #setting ceiling to array lenght for loop control of max #

    while (trips != 0):
        for count in range(floor, ceiling):
            if (iList[count] < lownum):
                lownum = iList[count]
                lownumindex = count
            elif (iList[count] > highnum):
                highnum = iList[count]
                highnumindex = count
        if ((iList[floor] == iList[highnumindex]) and (iList[lownumindex] != iList[ceiling-1]) ):
            (iList[highnumindex],iList[ceiling-1]) = (iList[ceiling-1],iList[highnumindex])
            (iList[floor],iList[lownumindex]) = (iList[lownumindex],iList[floor])
        elif ((iList[lownumindex] + iList[highnumindex]) == (iList[floor] + iList[ceiling-1])):
            (iList[floor],iList[lownumindex]) = (iList[lownumindex],iList[floor])
        elif ((iList[lownumindex] + iList[highnumindex]) != (iList[floor] + iList[ceiling-1])):
            (iList[floor],iList[lownumindex]) = (iList[lownumindex],iList[floor])
            (iList[highnumindex],iList[ceiling-1]) = (iList[ceiling-1],iList[highnumindex])
        
        floor += 1
        ceiling -= 1
        lownumindex = floor
        highnumindex = ceiling -1
        lownum = iList[lownumindex]
        highnum = iList[highnumindex]
        trips -= 1
        loopcounter += 1
    
    return iList

def selectionSort(iList):
    iterations = len(iList)
    lownum = iList[0]
    lownumindex = 0
    indexcounter = 0
    
    while (indexcounter != iterations-1):
        for count in range(indexcounter, iterations):
            if (iList[count] < lownum):
                lownum = iList[count]
                lownumindex = count
        
        print 'Counter array:', count
        (iList[indexcounter],iList[lownumindex]) = (iList[lownumindex],iList[indexcounter])
        indexcounter += 1
        lownum = iList[indexcounter]
        lownumindex = indexcounter
    return iList

#test list
list10 = [4, 16, 3, 2, 14, 11, 6, 8, 1, 15]
list9 = [4, 16, 3, 2, 14, 6, 8, 1, 15]
list4 = [4, 16, 1, 15]
listlong = [2085, 3080, 7389, 655, 1595, 91, 2226, 5615, 2839, 8360, 6589, 3427, 2066, 891, 9187, 5002, 5346, 
6487, 4933, 8577, 1570, 1732, 1023, 7697, 9184, 1157, 897, 4845, 6858, 4453, 2042, 7676, 7330, 2442, 1502, 
2773, 9664, 145, 2431, 4980, 4679, 3453, 6100, 5156, 2254, 3278, 1858, 7579, 9560, 5748, 1841, 3704, 1288, 
8285, 9013, 8226, 5325, 1040, 7978, 7896, 1905, 4604, 2259, 30, 9880, 7025, 3241, 6601, 502, 3403, 9932, 5657, 
626, 9703, 2270, 7867, 6422, 9098, 4737, 6515, 2412, 9155, 7995, 423, 8755, 5561, 8579, 5510, 201, 2527, 4122, 
606, 3754, 5259, 2437, 9672, 1297, 1208, 5266, 8431]

#test = random.sample(xrange(20), 10)
#test = random.sample(xrange(10000), 100)
start = datetime.datetime.now()
test = selectionSort(listlong)
end = datetime.datetime.now()
time = end-start
start2 = datetime.datetime.now()
test2 = selectionSortMax(listlong)
end2 = datetime.datetime.now()
time2 = end2-start2
print '\nYour list was selection sorted in:', time
print '\nYour list was selection sorted Max in:', time2
#print time.hour, 'hour(s) |', time.minute, 'minute(s) |', time.second, 'second(s) |', time.microsecond, 'microsecond(s)'
print '\nSelection Sort: \n',test
print '\nSelection Sort (Max):\n',test2




'''
Debug Archive
=============

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
# print 'The List is now:', iList, '\n'
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

def selectionSortMax(iList):
trips = len(iList)/2  
print 'Based on the length of the list:', len(iList), ' | The number of trips has been set to:', trips
lownum = iList[0]
lownumindex = loopcounter = floor = 0 #setting various counters to zero, floor controls loop for min #
highnum = iList[len(iList)-1]   #sets the last element as the inital high number for check
highnumindex = len(iList)-1     #sets index of high element to end for swap
ceiling = len(iList)    #setting ceiling to array lenght for loop control of max #
h = 'high' #temp variables to test list writing
l = 'low'   #temp variables to test list writing
while (trips != 0):
    print 'loop # ', loopcounter
    print 'lownum:', lownum
    print 'lownumindex:', lownumindex
    print 'highnum:', highnum
    print 'highnumindex:', highnumindex
    print 'Floor:', floor
    print 'Ceiling:', ceiling
    #print 'indexcounter:', loopcounter
    #print 'iterations:', iterations
    print 'The List is now:', iList, '\n'
    for count in range(floor, ceiling):
        if (iList[count] < lownum):
            print 'low number found at index:', count, ' and its value is', iList[count]
            lownum = iList[count]
            lownumindex = count
            print 'After update lownum:', lownum, 'and lownumindex:', lownumindex, '\n'
        elif (iList[count] > highnum):
            print 'High number found at index:', count, ' and its value is', iList[count]
            highnum = iList[count]
            highnumindex = count
            print 'After update highnum:', highnum, 'and highnumindex:', highnumindex, '\n'
    if ((iList[floor] == iList[highnumindex]) and (iList[lownumindex] != iList[ceiling-1]) ):
        print 'Dude this is going to break so im changing my swap order'
        print 'Swapping High(', iList[highnumindex], ',', iList[ceiling-1], ')'
        print 'Swapping Low (', iList[floor], ',', iList[lownumindex], ')'
        (iList[highnumindex],iList[ceiling-1]) = (iList[ceiling-1],iList[highnumindex])
        (iList[floor],iList[lownumindex]) = (iList[lownumindex],iList[floor])
    elif ((iList[lownumindex] + iList[highnumindex]) == (iList[floor] + iList[ceiling-1])):
        print 'Last sort position, only one swap needed'
        print 'Swapping Middle of List(', iList[floor], ',', iList[lownumindex], ')'
        (iList[floor],iList[lownumindex]) = (iList[lownumindex],iList[floor])
    elif ((iList[lownumindex] + iList[highnumindex]) != (iList[floor] + iList[ceiling-1])):
        print 'Swapping Low (', iList[floor], ',', iList[lownumindex], ')'
        print 'Swapping High(', iList[highnumindex], ',', iList[ceiling-1], ')'
        (iList[floor],iList[lownumindex]) = (iList[lownumindex],iList[floor])
        (iList[highnumindex],iList[ceiling-1]) = (iList[ceiling-1],iList[highnumindex])
    

    # debug line to add text to see how loop collapse on iterations
    # iList[lownumindex] = l
    # iList[highnumindex] = h
    # indexcounter += 1
    # iterations -= 1
    # lownum = iList[indexcounter]
    # lownumindex = indexcounter
    # highnum = iList[iterations-1]
    floor += 1
    ceiling -= 1
    lownumindex = floor
    highnumindex = ceiling -1
    lownum = iList[lownumindex]
    highnum = iList[highnumindex]
    trips -= 1
    loopcounter += 1
return iList

'''