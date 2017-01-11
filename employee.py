import random

class Employee:

	def __init__(self, firstName, lastName):
		self.firstName = firstName
		self.lastName = lastName

	def eat(self, food = None, companions = None):
		restaurants = ['PFChangs', 'bambooPalace', 'Obies', 'Giovanis']
		current_restaurant = restaurants[random.randint(0,3)]
		if food != None and companions == None:
			print('{} {} ate {} at the office'.format(self.firstName, self.lastName, food))
		elif companions != None and food == None:
			print('{} {} ate at {}'.format(self.firstName, ''.join(companions), current_restaurant))
		elif food != None and companions != None:
			print('{} {} ate {} at {}'.format(self.firstName, ''.join(companions), food, current_restaurant))
		else:
			print('{} {} ate at {}'.format(self.firstName, self.lastName, current_restaurant))
			return current_restaurant

jack = Employee('jack', 'pinkston')
jack.eat('pizza', companions = ['nick ', 'steve ', 'drew '])
