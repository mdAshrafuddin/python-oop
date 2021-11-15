class Employee:
    # constructor
    def __init__(self, name, salary):
        # Public data member
        self.name = name
        # Private member
        self.__salary = salary

# Creating object of a method
emp = Employee('AShraf', 300)
emp.show()
print('Salary ', emp.__salary)