from employee import Employee

class Developer(Employee):
    """class for who report to the manager"""

    def __init__(self, name, salary, dev_language):
        super().__init__(name, salary) 
        
        self.dev_language = dev_language
        
    

    def __str__(self):
        return f"Developer: {self.dev_language}."