#Inheritence class EX#1
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Matee', 'rehman', 50000, 'Python')
dev_2 = Developer('Wasif', 'Ali', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()


#Inheritence class EX#2
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")



class Car(Vehicle):
    def __init__(self, brand, model, modelnum):
        super().__init__(brand, model)
        self.modelnum = modelnum

    def show_info(self):
        super().show_info()
        print(f"Model Num: {self.modelnum}")


class Bike(Vehicle):
    def __init__(self, brand, model, cc):
        super().__init__(brand, model)
        self.cc = cc

    def show_info(self):
        super().show_info()
        print(f"Engine Capacity: {self.cc}cc")



car1 = Car("Toyota", "Corolla", 2024)
bike1 = Bike("Honda", "CBR", 600)


print("Car Details:")
car1.show_info()

print("\nBike Details:")
bike1.show_info()

