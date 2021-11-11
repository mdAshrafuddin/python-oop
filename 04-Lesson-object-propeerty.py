# Object Property
class Furit:
    # constructor
    def __init__(self, name, color):
        # instance method
        self.name = name
        self.color = color
    
    # instance method
    def show(self):
        # Access instance variable and class variable
        print('Furits is ', self.name, 'and Color is ', self.color)

# creating object of the class
obj = Furit('Apple', 'red')

# Modify the object property
obj.name = "Retina"

# call the instance method using the onject obj
obj.show()