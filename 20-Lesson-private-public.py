class Employee:
    # constructor
    def __init__(self, name, salary):
        # instance variable
        self.name = name
        self.__salary  = salary

    # public instance method
    def show(self):
        print('Name ', self.name, 'Salary ', self.__salary)
    
emp = Employee('AShraf', 3400)
emp.show()
    