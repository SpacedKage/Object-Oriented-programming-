class Employee:
    """The base class for all employees"""

    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def __str__(self):
        return f"Name: {self.name}."

   
   