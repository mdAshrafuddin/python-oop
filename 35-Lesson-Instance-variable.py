# How to create instance variable

class Student:
    # constructor 
    def __init__(self, name, age):
        # instance variable
        self.name = name
        self.age  = age
    
    # Calling instance method of instance variable
    def show(self):
        print('Name ', self.name, 'Age ', self.age)
    
    # modyfing instance method
    def update(self, change_name, age):
        self.name = change_name
        self.age = age

student = Student('AShraf', 23)

student.show()
student.update('Tasnjil', 34)
student.show()