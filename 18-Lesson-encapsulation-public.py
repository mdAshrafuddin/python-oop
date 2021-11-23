class Employee:
    # Contstructor
    def __init__(self, name, salary, proejct):
        # instance method
        self.name = name
        self.salary = salary
        self.project = proejct
    
    # Instance method
    def show(self):
        print('Name ', self.name, 'Salray is ', self.salary)
    
    def work(self):
        print('Name ', self.name, 'is working on ', self.project)

emp = Employee('Asharf', 2340, 'Pla')

# Calling public method of the class
emp.show()
emp.work()

