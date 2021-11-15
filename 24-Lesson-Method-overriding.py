class Vehicle:
    def __init__(self, speed, change_grear):
        # instance variable for vehicle
        self.speed = speed
        self.change_grear = change_grear

    def show(self):
        print('Details ', self.speed, self.change_grear)
    
    def max_speed(self):
        print('Vehicle max speed is 150')
    
    def change_speed(self):
        print('Vehicle change 6 gear')

# Inherit form vehicle class
class Car(Vehicle):
    def max_speed(self):
        print('Car max speed is 240')
    def change_speed(self):
        print('Car change 10 gear')

# Car Object
car = Car('Car x1 ', 30)
car.show()
car.max_speed()
car.change_speed()

# vehicle object
vehicle = Vehicle('vehicle x1', 30)
vehicle.show()
vehicle.max_speed()
vehicle.change_speed()