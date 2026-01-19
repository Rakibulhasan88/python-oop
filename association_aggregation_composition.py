#Association
'''
class Laptop:
    def __init__ (self, brand):
        self.brand = brand
    
class Student:
    def __init__(self, name, laptop_obj):
        self.name = name
        self.laptop_v = laptop_obj
    
    def show_laptop_info(self):
        print(f"{self.name} has a {self.laptop_v.brand}")
        
lp1 = Laptop("Asus")
student = Student("Rakib",lp1)
student.show_laptop_info()

'''


# Aggregation : has a relationship
# A university has departments.
'''
class Department:
    def __init__(self, name):
        self.name = name
    
class University:
    def __init__ (self, name):
        self.name = name
        self.departments = []
        
    def add_departments(self, department):
        self.departments.append(department)
        
    def show_departments(self):
        return [department.name for department in self.departments]
    
uni1 = University("Daffodil International University")
dep1 = Department("Computer Science")
dep2 = Department("Business Administration")
uni1.add_departments(dep1)
uni1.add_departments(dep2)
print(uni1.show_departments())

'''


# Composition : part of relationship
# A car has an engine.
# Every class must be defined inside the other class.

class Engine:
    def __init__(self, power):
        self.power = power

class Car:
    def __init__ (self, model,power):
        self.model = model
        self.engine = Engine(power)
        
    def show_details(self):
        print(f"{self.model}has an enginre with {self.engine.power}HP")
        
car = Car("Toyota",100)
car.show_details()