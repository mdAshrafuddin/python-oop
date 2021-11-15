class Student:
    def  __init__(self, name, roll_no, age):
        self.name = name
        self.__roll_no = roll_no
        self.__age     = age

    def show(self):
        print('Student Details : ', self.name, self.__roll_no, self.__age)
    
    def get_roll_no(self):
        return self.__roll_no

    def set_roll_no(self, number):
        if number > 50:
            print('Invalid roll no . Please set correct roll number')
        else:
            self.__roll_no = number

ashraf = Student('AShraf', 10, 14)
ashraf.show()
ashraf.set_roll_no(120)
ashraf.set_roll_no(34)
ashraf.show() 