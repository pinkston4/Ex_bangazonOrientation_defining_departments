from definingDepartments import *

class HumanResources(Department):
  """Class for representing Human Resources department

  Methods: __init__, add_policy, get_policy, etc.
  """

  def __init__(self, name, supervisor, employee_count, budget):
    super(HumanResources, self).__init__(name, supervisor, employee_count, budget)
    self.policies = set()

  def add_policy(self, policy_name, policy_text):
    """Adds a policy, as a tuple, to the set of policies

    Arguments:
      policy_name (string)
      policy_text (string)
    """

    self.policies.add((policy_name, policy_text))

  def get_policy(self):
    return self.policies

  def get_budget(self, budget):
    super(Dev, self).get_budget(budget)
    return self.budget

 

hr_department = HumanResources('those_people', 'God', 'to many', 10000)
hr_department.add_policy('thingy', 'thingythingythingy')
print(hr_department.policies)