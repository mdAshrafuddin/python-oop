class Student:
    def __init__(self, name):
        print('One arguments constructor')
        self.name = name
    
    def __init__(self, name, age):
        print('two arguments constructor')
        self.name = name
        self.age = age

ashraf = Student('AShraf')

tanjil = Student('Tanjil', 34)
