class Student:
    school_name = 'Ashraf School'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print('Name ', self.name, 'Age ', self.age, 'School Name ', Student.school_name)
    
    @classmethod
    def change_school(self, school_name):
        self.school_name  = school_name

student = Student('AShraf', 234)
student.show()
student.change_school('Tanjil School Name')
student.show()