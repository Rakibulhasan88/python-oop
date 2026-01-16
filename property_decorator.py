class Employee:
    company_name = "Ostad Company"
    def __init__ (self, name, salary):
        self.name = name
        self._salary = salary
        
    @property
    def get_salary(self):
        return self._salary

ob1 = Employee("Rakib", 50000)
print(ob1.get_salary)
print(ob1.get_salary)