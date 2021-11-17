# Parent class 1
class Person:
    def person_info(self, name, age):
        print('Inside Person class')
        print('Name', name, 'Age ', age)
    
# Parent class 2
class Company:
    def company_info(self, company_name, location):
        print('Inside Company class')
        print('Company name ', company_name, 'Location ', location)

class Employee(Person, Company):
    def Employee_info(self, salary, skills):
        print('Inside Employee class')
        print('salary ', salary, 'skills ', skills)

employee = Employee()
employee.person_info('AShraf', 34)
employee.company_info('AShrafBd', 'DHAKA')
employee.Employee_info(3454, 'HTML')