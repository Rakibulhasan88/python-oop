# class Singleton:
#     _instance = None
    
#     def __new__(cls):
#         if cls._instance is None:
#             cls.instance = super(Singleton, cls).__new__(cls)
#         return cls._instance

# ob1 = Singleton()
# ob2 = Singleton()

# print(ob1 is ob2)  # True

'''
# Factory Method Pattern
class Car:
    def driver(self):
        return "Driving a car"
class Bike:
    def driver(self):
        return "Riding a bike"
class VehicleFactory:
    @staticmethod
    def get_vehicle(type):
        if type == "car":
            return Car()
        elif type == "bike":
            return Bike()
        else:
            return ValueError("Unknown vehicle type")

vehicle = VehicleFactory.get_vehicle("bike")
print(vehicle.driver())
'''
# Builder Pattern

class Computer:
    def __init__(self, cpu, ram, storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
    def __str__(self):
        return f"Computer with {self.cpu} CPU, {self.ram} RAM, {self.storage} STORAGE."

class ComputerBuilder:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        
    def set_cpu(self, cpu):
        self.cpu = cpu
        return self
    
    def set_ram(self, ram):
        self.ram = ram
        return self
        
    def set_storage(self, storage):
        self.storage = storage
        return self
    
    def build(self):
        return Computer(self.cpu, self.ram, self.storage)
    
builder = ComputerBuilder()
computer = builder.set_cpu("intel i9").set_ram("32GB").set_storage("1TB SSD").build()
print(computer)
    