class Department(object):
    """Parent class for all departments

    Methods: __init__, get_name, get_supervisor
    """

    def __init__(self, name, supervisor, employee_count):
        self.name = name
        self.supervisor = supervisor
        self.size = employee_count

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