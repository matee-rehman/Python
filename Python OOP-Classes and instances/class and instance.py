#Creating instances of a class manually
class Employee:
   pass

emp_1=Employee()
emp_2=Employee()

print(emp_1)
print(emp_2)

emp_1.name='Matee'
emp_1.degree='compsci'
emp_1.age=22
emp_1.email='matee.compsci@umt.pk'

emp_2.name='yasir'
emp_2.degree='compsci'
emp_2.age=23
emp_2.email='yasir.compsci@umt.pk'

print(emp_1.email)
print(emp_2.email)

#creating instances by init method

class Employee:
   def __init__(self,name,degree,age):
      self.name=name
      self.degree=degree
      self.age=age
      self.email=name + '.' + degree +'@umt.com'
      

emp_1=Employee('Matee','compsci',22,)
emp_2=Employee('yasir','arts',23)

print(emp_1)
print(emp_2)

print(emp_1.email)
print(emp_2.email)

#

class Employee:
   def __init__(self,name,degree,pay):
      self.name=name
      self.degree=degree
      self.pay=pay
      self.email=name + '.' + degree +'@umt.com'
      

   def apply_raise(self):
     self.pay=int(self.pay * 1.04)

emp_1=Employee('Matee','compsci',22000)
emp_2=Employee('yasir','arts',23000)

print(emp_1.pay)
emp_1.apply_raise()




