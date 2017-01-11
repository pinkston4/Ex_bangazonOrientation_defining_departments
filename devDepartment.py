from definingDepartments import *

class Dev(Department):
	'''Class for representing the development department
	Methods:
		add_language
		get_language
	'''

	def __init__(self, name, supervisor, employee_count, budget):
		super(Dev, self).__init__(name, supervisor, employee_count, budget)
		self.languages = []

	def add_language(self, language):
		'''Add language to list
		argument:
			single argument of language you want to add onto languages
		'''
		self.languages.append(language)

	def get_language(self):
		return self.languages 

	def get_budget(self, budget):
		super(Dev, self).get_budget(budget)
		return self.budget
		
	  

jack_dev = Dev('Developer', 'Steve', 28, 10000)
print(jack_dev.budget)
print(jack_dev.name)

jack_dev.add_language('python')
jack_dev.add_language('javascript')
print(jack_dev.get_language())

print(jack_dev.get_budget(1000))
print(jack_dev.budget)
