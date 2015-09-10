import random 	#random num library
heads = 0	#heads counter, heads are 1's once rounded
tails = 0 	#tails counter, tails are 0's once rounded


for count in range(1,5001):
	toss = random.random()
	toss = round(toss)
	if toss == 1:
		heads += 1
		coin = "It's a head!"
	else:
		tails += 1
		coin = "It's a tail!"
	print 'Attempt #'+str(count)+': Throwing a coin...', coin, 'Got', str(heads), 'head(s) so far and', str(tails), 'tail(s) so far'
