# class Singleton:
#     _instance = None
    
#     def __new__(cls):
#         if cls._instance is None:
#             cls.instance = super(Singleton, cls).__new__(cls)
#         return cls._instance

# ob1 = Singleton()
# ob2 = Singleton()

# print(ob1 is ob2)  # True

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
    