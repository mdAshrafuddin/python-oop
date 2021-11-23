class Student:
    school_name = 'Chunarughat School'

    def __init__(self, name):
        self.name = name
        # Access class variable inside constructor using self
        print(self.school_name)
        # Access using class name
        print(Student.school_name)

student = Student('Ashraf')
print(student.name)