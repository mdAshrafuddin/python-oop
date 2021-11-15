class Ferrari:
    def fuel_type(self):
        print("Petrol")
    def max_speed(self):
        print('max speed 240')

class BMW:
    def fuel_type(self):
        print("Diesel")
    def max_speed(self):
        print('max speed 340')

ferrari = Ferrari()
bmw = BMW()

for car in (ferrari, bmw):
    car.fuel_type()
    car.max_speed()
