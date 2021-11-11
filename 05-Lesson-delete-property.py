class Fruit:
    def __init__(self, name, color):
        self.name = name 
        self.color = color
    
    def show(self):
        print('Fruit name ', self.name, 'and color is ', self.color)
    
obj = Fruit('Banana', 'yellow')

# delete oject property
del obj.name
obj.show()

# Delete Objects
del obj

obj.show()