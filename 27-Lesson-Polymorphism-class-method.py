# class Ferrari:
#     def fuel_type(self):
#         print("Petrol")
#     def max_speed(self):
#         print('max speed 240')

# class BMW:
#     def fuel_type(self):
#         print("Diesel")
#     def max_speed(self):
#         print('max speed 340')

# ferrari = Ferrari()
# bmw = BMW()

# for car in (ferrari, bmw):
#     car.fuel_type()
#     car.max_speed()

class Ferari:
    def fuel_type(self):
        print('fuel type Ferari')

    def  max_speed(self):
        print('max speed')

class Car(Ferari):

    def fuel_type(self):
        print('fuel type Ferari')

    def  max_speed(self):
        print('max speed')

def full_fun(obj):
    obj.fuel_type()
    obj.max_speed()

ferari = Ferari()
car = Car()

full_fun(ferari)
full_fun(car)

# for n in (ferari, car):
#     ferari.fuel_type()
#     car.max_speed()

students = ['Emma', 'Jessa', 'Kelly']
school = 'ABC School'

print('Reversed list')
for i in reversed(students):
    print(i, end='')

print('\n Reversed string')
for n in reversed(school):
    print(n, end='')


def add(a, b):
    c = a + b
    print(c)

def add(a, b, n):
    d = a + b + n
    print(d)

# first mehod is error
# add(3, 4)
# it is working
add(3, 4, 5)
    
for i in range(5): print(i, end=', ')
print()
for i in range(5, 10): print(i, end=', ')
print()
for i in range(2, 12, 2): print(i, end=', ')
print('\n')
class Shape:
    def area(self, a, b = 0):
        if b > 0:
            print('Area of Rectangle is ', a*b)
        else:
            print('Area is square ', a ** 2)

shape = Shape()
shape.area(5, 1)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, timesheet):
        print('Worked for', timesheet.days, 'days')
        # calculate salary
        return self.salary * timesheet.days


class TimeSheet:
    def __init__(self, name, days):
        self.name = name
        self.days = days


emp = Employee("Jessa", 800)
timesheet = TimeSheet("Jessa", 50)
print("salary is: ", emp * timesheet)

# Overloading + operator for custom objects
class Book:
    def __init__(self, pages):
        self.pages = pages
    
    def __mul__(self, timesheet):
        return self.pages * timesheet.days

class TimeSheet:
    def __init__(self, days):
        self.days = days
    
b1 = Book(33)
b2 = TimeSheet(45)

print(b1 * b2)