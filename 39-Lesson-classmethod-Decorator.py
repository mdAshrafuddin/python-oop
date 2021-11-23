from datetime import date

class Student:
    
    school_name = "XYZ School"
    
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    
    def show(self):
        print('Name ', self.name, 'Roll No ', self.roll_no)

    
    @classmethod
    def classMethod(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)

jessa = Student('Jessa', 20)
jessa.show()

ashraf = Student.classMethod('Ashraf', 1994)

ashraf .show()