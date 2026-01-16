class Employee:
    cmopany_name = "Ostad Company"
    def __init__ (self, name, salary):
        self.name = name
        self._salary = salary
        
    def get_salary(self, password):
        if password == "Admin":
            print(self._salary)
        else:
            print("Invalid Access")
            
    def set_salary(self, password, salary):
        if password == "Admin":
            self._salary = salary
            print(f"New Salary : {self._salary}")
        else :
            print("Invalid Access!!")
        
ob1 = Employee("Rakib", 50000)
ob2 = Employee("Hasan", 70000)

# ob1.get_salary("Admin")
ob1.set_salary("Admin", 60000)

