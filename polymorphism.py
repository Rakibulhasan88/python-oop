# Poly -> multiple
# Morphism -> forms

# Method Overriding
class GrandFather:
    def greet(self):
        print("Father says: Hello!")
class Father(GrandFather):
    def greet(self):
        print("Father says: Hi!")

class Childeren(Father):
    def greet(self):
        print("Children says: Hey!")
        
grandfather = GrandFather()
father = Father()
children = Childeren()

grandfather.greet()
father.greet()
children.greet()

# Method Overloading
class Shape:
    def area(self,a,b=10):
        return a * b
        
p = Shape()
print(p.area(12))