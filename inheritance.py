# Single inheritance

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
