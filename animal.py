class Animal(object):
	def __init__(self, health=100, name='Animal'):
		self.name = name
		self.health = health

	def walk(self, strides=1):
		if (strides <= 0):
			print 'No such things as negative running, get your shit together'
			return self
		for count in range(strides):
			self.health -= 1
		return self

	def run(self, strides=1):
		if (strides <= 0):
			print 'No such things as negative running, get your shit together'
			return self
		for count in range(strides):
			self.health -= 10
		return self

	def displayHealth(self):
		print self.name, 'has a health of:', self.health
		return self

	def pet(self):
		return self

class Dog(Animal):
	def __init__(self, name='Dog'):
		super(Dog, self).__init__()
		self.health = 150
		self.name = name

	def pet(self, times=1):
		if (times <= 0):
			print 'No such things as not petting an animal'
			return self
		for count in range(times):
			self.health += 5
		return self

class Dragon(Animal):
	def __init__(self, name='Dragon'):
		super(Dragon, self).__init__()
		self.health = 170
		self.name = name

	def fly(self, times):
		if (times <= 0):
			print 'No such things as not petting an animal'
			return self
		for count in range(times):
			self.health -= 10
		return self

	def displayHealth(self):
		print 'This is a Dragon\n'
		super(Dragon, self).displayHealth()
		return self




animal = Animal()
animal.walk(3).run(2).displayHealth()

mj = Dog('MJ')
mj.walk(3).run(2).pet().displayHealth()

drago = Dragon('Drago')
drago.walk(3).run(2).fly(2).displayHealth()
