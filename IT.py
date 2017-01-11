from definingDepartments import *

class IT(Department):
	'''Class for representing the development department
	Methods:
		add_technology
		get_technology
	'''

	def __init__(self, name, supervisor, employee_count):
		super(IT, self).__init__(name, supervisor, employee_count)
		self.technologies = []

	def add_technology(self, language):
		'''Add language to list
		argument:
			single argument of language you want to add onto technologies
		'''
		self.technologies.append(language)

	def get_technology(self):
		return self.technologies 

jack_tech = IT('IT', 'Steve', 28)
print(jack_tech.name)

jack_tech.add_technology('python')
jack_tech.add_technology('javascript')
print(jack_tech.get_technology())