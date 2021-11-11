# Delete property

# create clasas name
class Employee:
    # class variable
    department_name = "CSE"

    # constructor
    def __init__(self, name):
        # instance variable
        self.name = name
    # instance method
    def show(self):
        print('Name ', self.name, 'Department name is ', self.department_name)

emp = Employee('AShraf Uddin')

emp.show()

del emp

emp.show()