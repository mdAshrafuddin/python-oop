class Employee:
    def __init__(self, name, salary):
        self.name =  name
        self.__salary = salary


emp = Employee('AShraf', 300)

print('Name ', emp.name)

print('Salary ', emp._Employee__salary)