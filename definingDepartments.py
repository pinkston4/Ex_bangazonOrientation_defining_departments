class Department(object):
    """Parent class for all departments

    Methods: __init__, get_name, get_supervisor
    """

    def __init__(self, name, supervisor, employee_count, budget):
        self.name = name
        self.supervisor = supervisor
        self.size = employee_count
        self.budget = budget

    def get_name(self):
      """Returns the name of the department"""

      return self.name

    def get_supervisor(self):
      """Returns the name of the supervisor"""

      return self.supervisor

    def set_name(self):
      self.name = name

    def set_supervisor(self):
      self.supervisor = supervisor

    def get_budget(self, new_budget):
      self.budget = new_budget
      return self.budget

    def meet(self):
      print("everyone meet in {}'s office for the meetings".format(self.supervisor))