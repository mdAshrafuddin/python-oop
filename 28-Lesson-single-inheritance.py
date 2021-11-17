# Base class
class Vehicle:
    def vehicle_info(self):
        print('Inside Vehicle class')

# Child class 
class Car(Vehicle):
    def car_info(self):
        print('Inside car class')

# Called object of car
car = Car()

# Access Vehicle's info using car object
car.vehicle_info()
car.car_info()

