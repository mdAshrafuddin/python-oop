class Company:

    # no-argument constructor
    def __init__(self):
        self.name = "Ashraf"
        self.address = 'Chunarughat'
    
    # a method for printing data members
    def show(self):
        print('Name : ', self.name, 'Addess : ', self.address)

# Creating object of the class
company = Company()

# calling the instance method  using the object
company.show()