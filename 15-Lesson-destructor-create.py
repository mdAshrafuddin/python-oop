# import time

# class Student:
#     # constructor
#     def __init__(self, name):
#         print('Inside constructor')
#         self.name = name
#         print('Object initialized')
    
#     def show(self):
#         print('Hello, my name is ', self.name)

#     # destructor
#     def __del__(self):
#         print('Inside destructor')
#         print('Object destructor')

# ashraf = Student('Ashraf')
# s2 = ashraf

# ashraf.show()

# del ashraf

# time.sleep(5)
# print('After sleep')
# s2.show()

import time

class A:
    def __init__(self, name):
        print('Inside the constructor')
        self.name = name

    def show(self):
        print('Name ', self.name)

    def __del__(self):
        print(self.name)

class B():
    def __init__(self,id):
        print('Inside the constructor')
        self.id = id

    def show(self):
        print('id ', self.id)

    
    def __del__(self):
        print(self.id)

# a = A('Ashraf')
b = B(234)
# a.show()
b.show()

del b
time.sleep(5)
# b.show()