class Employee:
    # parameterized constructor
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    # instance method
    def show(self):
        print('Name : ', self.name, 'address : ', self.address)
    
employee = Employee('AShraf', 'Chunarughat')
employee.show()
    
