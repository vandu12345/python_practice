
class Man():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def walk(self):
        print("Walking")
    
    def run(self):
        print("running")
    
    def check_all_function(self):
        self.walk()
        self.run()
        
    
    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    
class Subho():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def walk(self):
        print("Special Walking")
        


class MiniSubhoo(Subho, Man):
    def __init__(self, name, age):
        super().__init__(name, age)
        super().__init__(name, age) 
    
    
        
print(MiniSubhoo.__mro__)

subho = MiniSubhoo(name="test", age=19)


print(subho)
subho.walk()

# print(subho.age)
# print(subho.name)
