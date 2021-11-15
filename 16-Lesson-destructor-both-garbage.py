import time

class Vehicle():
    def __init__(self, id, car):
        self.id = id
        self.dealer = car
        print('Vehile ', self.id, 'created')
    
    def __del__(self):
        print('Vechile ', self.id, 'destroyed')

class Car():
    def __init__(self, id):
        self.id = id;
        # saving Vehicle class object in 'dealer' variable
        # Sending reference of Car object ('self') for Vehicle object
        self.dealer = Vehicle(id, self);
        print('Car', self.id, 'created')

    def __del__(self):
        print('Car', self.id, 'destroyed')


# create car object
c = Car(12)
# delete car object
del c
# ideally destructor must execute now

# to observe the behavior
time.sleep(8)