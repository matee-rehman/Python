#Property Decorator
class Employee:
    def __init__(self, name, degree):
        self.name = name
        self.degree = degree
    @property  
    def email(self):
        return '{}.{}@umt.com'.format(self.name, self.degree)
    @property
    def full_name(self):
        return '{} {}'.format(self.name, self.degree)


emp_1 = Employee('Matee', 'compsci')
emp_2 = Employee('Yasir', 'arts')

emp_1.name = 'waif'

print(emp_1.name)
print(emp_1.full_name)

#Setter

class Employee:
    def __init__(self, name, degree):
        self.name = name
        self.degree = degree

    @property  
    def email(self):
        return '{}.{}@umt.com'.format(self.name, self.degree)

    @property
    def full_name(self):
        return '{} {}'.format(self.name, self.degree)
    
    @full_name.setter
    def full_name(self, fullname):
        parts = fullname.split(' ')
        if len(parts) == 2:
            self.name, self.degree = parts
        else:
            raise ValueError("Full name must include both name and degree separated by a space.")

emp_1 = Employee('Matee', 'compsci')

emp_1.full_name = 'Waif Arts'   

print(emp_1.name)        
print(emp_1.degree)      
print(emp_1.email)      
print(emp_1.full_name)   

