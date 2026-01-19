# Single inheritance
'''
class GrandFather:
    def __init__ (self, color, first_name):
        self.color = color
        self.first_name = first_name
        
class Father(GrandFather):
    def __init__ (self,hobby, color, first_name):
        super().__init__ (color, first_name)
        self.hobby = hobby
        

gf1 = GrandFather("White","Rakib")
f1 = Father("Football", "Red", "Hasan")
print(f1.first_name)
print(gf1.first_name)
'''

# Multiple Inheritance
class GrandFather:
    def __init__ (self, color, first_name):
        self.color = color
        self.first_name = first_name
        
    def gf_method(self):
        print("I am from GrandFather class")
        
class Father(GrandFather):
    def __init__ (self,hobby, color, first_name):
        super().__init__ (color, first_name)
        self.hobby = hobby
        
    def father_method(self):
        print("I am from Father class")
        
class Children(Father, GrandFather):
    def __init__(self, feshion , hobby, color, first_name):
        super().__init__(hobby, color, first_name)
        self.feshion = feshion
        
    def children_method(self):
        print("I am from Children class")

# gf1 = GrandFather("White","Rakib")
# f1 = Father("Football", "Red", "Hasan")
# print(f1.first_name)
# print(gf1.first_name)

c1 = Children("Modern", "Cricket", "Black", "Khan")
c1.father_method()
print(c1.first_name)
