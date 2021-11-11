class Student:
    # class variables
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age  = age
    
s1 = Student('AShraf', 27)
# Instance varialbes
print('Student ', s1.name, s1.age)

# class variables
print('School name ', Student.school_name)