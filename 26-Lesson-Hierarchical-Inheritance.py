class Vehicle:
    def info(self):
        print("This is Vehicle")

class Car(Vehicle):
    def car_info(self):
        print("This is Car")

class Truck(Vehicle):
    def truck_info(self):
        print("This is Truck")

car = Car()
car.info()
car.car_info()

truck = Truck()
truck.info()
truck.truck_info()
