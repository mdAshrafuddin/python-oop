# How to create class
class Person:
    def __init__(self, name, gender, profession):
        # data members(instance variables)
        self.name = name
        self.gender  = gender
        self.profession = profession

    # Beahvior(instance method)
    def show(self):
        print('Name : ', self.name, 'Gender : ', self.gender, 'Profession : ', self.profession)
    
    # Behavior(Instance method)
    def work(self):
        print(self.name, 'working as a', self.profession)

# create object of a class
ashraf = Person('Ashraf', 'Male', 'Web developer')

# modify the instance variable
ashraf.name = "Tanjil"

# call method
ashraf.show()
ashraf.work()


