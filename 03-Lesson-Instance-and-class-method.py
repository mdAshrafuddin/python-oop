#Exmaple-03 Define and call an instance method and class method

# create class demo
class Student:
    # class variable
    school_name = 'Chandupur School'
    # constructor
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age  = age
    
    # instance method
    def show(self):
        # Access instance variable and class variables
        print('Name: ', self.name, 'Age: ', self.age, 'School name: ', Student.school_name)
    
    # instance mehtod
    def change_age(self, newAge):
        # Modify the instance variable
        self.age = newAge
    
    # class method
    @classmethod
    def modify_school_name(cls, new_name):
        cls.school_name = new_name

# Object Create
student = Student('AShraf', 23)
# call instance method
student.show()
student.change_age(34)

# call class method
Student.modify_school_name('ASB School')

# call instance method
student.show()
