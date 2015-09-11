class car(object):
	def __init__(self, price=0, speed='', fuel=10, miles=5000):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.miles = miles
		self.tax()
		self.displayAll()

	def displayAll(self):
		print 'This car cost:', self.price, 'goes', self.speed, 'mph while getting ', self.fuel, 'miles per gallon and currently only has', self.miles, 'miles!\n'

	def tax(self):
		if (self.price > 10000):
			self.tax = .15
		else:
			self.tax = .12

car1 = car(15000, '100mph', 27, 30000)
car2 = car(15000, '160mph', 20, 600)
car3 = car(15000, '200mph', 17, 2000)
car4 = car(15000, '30mph', 50, 30)
car5 = car(15000, '60mph', 70, 599)