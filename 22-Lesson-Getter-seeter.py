class Student:
    def __init__(self, name, age):
        # Private memeber
        self.name = name
        self.__age  = age
    
    # Getter Method
    def get_age(self):
        return self.__age

    # Setter method
    def set_age(self, age):
        self.__age = age
    
stud = Student('Tanjil', 34)

print('Name : ', stud.name, stud.get_age())

stud.set_age(16)

print('Name : ', stud.name, stud.get_age())
    
