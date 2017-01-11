from definingDepartments import *

class IT(Department):
	'''Class for representing the development department
	Methods:
		add_technology
		get_technology
	'''

	def __init__(self, name, supervisor, employee_count, budget):
		super(IT, self).__init__(name, supervisor, employee_count, budget)
		self.technologies = []

	def add_technology(self, language):
		'''Add language to list
		argument:
			single argument of language you want to add onto technologies
		'''
		self.technologies.append(language)

	def get_technology(self):
		return self.technologies 

	def get_budget(self, budget):
		super(Dev, self).get_budget(budget)
		return self.budget

	def meet(self):
		print('everyone meet in the server room')
	

jack_tech = IT('IT', 'Steve', 28, 10000)
print(jack_tech.name)

jack_tech.add_technology('python')
jack_tech.add_technology('javascript')
print(jack_tech.get_technology())

print(jack_tech.meet())

