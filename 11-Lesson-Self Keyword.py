class Student:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    # Self point to the current object
    def show(self):
        # access instance variable using self
        print(self.name, self.age)

# Creating first object
ashraf = Student('Ashraf', 34)
ashraf.show()

# creating secound object
tanjil = Student('Tanjil', 27)
tanjil.show()