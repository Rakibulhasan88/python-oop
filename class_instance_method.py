class Employee:
    company_name = "Osatad tec"
    
    def __init__ (self, name, salary):
        self.name = name
        self.salary = salary
    
    def display_info(self):
        print(f"Employee Name: {self.name}\nSalary: {self.salary}")
    
    @classmethod    
    def change_company_name(cls, name):
        cls.company_name = name
        
ob1 = Employee("Rakib", 50000)
ob1.display_info()
# ob1.change_company_name("Daffodil School")
print(ob1.company_name)