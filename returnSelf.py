class bike(object):
	def __init__(self, price=19.99, speed="25mph", miles=0):
		self.price = price
		self.max_speed = speed
		self.miles = miles

	def displayInfo(self):
		print 'The bike cost: $'+str(self.price)+' goes a top speed of '+self.max_speed, 'and has been riden ', self.miles, 'miles!'
		return self
		
	def ride(self, rides=1):
		if (rides <= 0):
			print 'No such things as negative riding, get your shit together'
			return self
		for count in range(rides):
			print 'Currently Riding'
		self.miles += (10*rides)
		return self

	def reverse(self, rides=1):
		if (rides <= 0):
			print 'No such things as negative reversing, get your shit together'
			return self
		else:
			if (self.miles == 0):
				print 'Noting to reverse, try going for a ride'
			elif (self.miles < 0):
				print 'Dude what kind of scam are you running, come on SON ;)'
			elif (self.miles <= 10):
				print 'This bike is brand new, why you screwing with it????. I reset the value anyway'
				self.miles = 0
			else:
				for count in range(rides):
					print 'Currently reversing the mileage even though this is illegal in most states!'
				self.miles -= (10*rides)
		return self

puegot = bike(200.00, '100mph')
puegot.ride(3).reverse().displayInfo()

bmx = bike(150, '30mph')
bmx.ride(2).reverse(2).displayInfo()

cruiser = bike(350.59, '15mph')
cruiser.reverse(3).displayInfo()

raw_input('\n\nPress Enter to Check Error Catching')
error1 = bike(99,'tester',-10)
error2 = bike(99,'tester',0)
error3 = bike(99,'tester',5)
error1.reverse()
error2.reverse()
error3.reverse()
