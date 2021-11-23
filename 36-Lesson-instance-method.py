# How to create instance Method

class Student:
    # constructor 
    def __init__(self, name, age):
        # instance variable
        self.name = name
        self.age  = age
    
    # Instance method
    def show(self):
        print('Name ', self.name, 'Age ', self.age)
    
    # upadated instance method
    def update(self, change_name, change_age):
        self.name = change_name
        self.age  = change_age
    
    def add(self, mark):
        self.mark = mark

student = Student('Tanjil', 34)
student.show()
student.add(34)
student.update('Ashraf Uddin', 45)
student.show()
# del student.show
delattr(student, 'show')
student.show()
# print('Name ', student.name, 'Age ', student.age, 'Make ', student.mark)