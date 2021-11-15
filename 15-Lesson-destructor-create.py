import time

class Student:
    # constructor
    def __init__(self, name):
        print('Inside constructor')
        self.name = name
        print('Object initialized')
    
    def show(self):
        print('Hello, my name is ', self.name)

    # destructor
    def __del__(self):
        print('Inside destructor')
        print('Object destructor')

ashraf = Student('Ashraf')
s2 = ashraf

ashraf.show()

del ashraf

time.sleep(5)
print('After sleep')
s2.show()