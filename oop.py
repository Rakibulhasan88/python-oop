class Car:
    # def __init__(self):
    #     self.brand = ""
    #     self.model = ""
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")
        
car1= Car("Toyota","Corolla")
# car1.brand = "Toyota"
# car1.model = "Corolla"
# print(car1.brand)  
# print(car1.model)
car1.display_info()

car2=Car()
car2.display_info()

# print(car2.brand)
# print(car2.model)        