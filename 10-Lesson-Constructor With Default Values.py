# Create class name
class Student:
    # default constructor default value
    def __init__(self, name, age = 23, address = 'Chunarughat'):
        self.name = name
        self.age  = age 
        self.address = address
    
    def show(self):
        print('Name ', self.name, 'Age ', self.age, 'address ', self.address)

student = Student('AShraf', 45, 'Habiganj')
student.show()