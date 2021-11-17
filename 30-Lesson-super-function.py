class Vehicle:
    def company_name(self):
        return "Google"

class Car(Vehicle):
    def info(self):
        c_name = super().company_name()
        print('AShraf works at ', c_name)
        
car = Car()
car.info()