# Base class
class Vehicle:
    def vehicle_info(self):
        print('Inside vehicle class')

class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')

class SportsCar(Car):
    def sportsCar_info(self):
        print('Inside Sports Car class')

car = Car()
car.vehicle_info()
car.car_info()

sportsCar = SportsCar()
sportsCar.sportsCar_info()