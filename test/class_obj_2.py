class Car():
    def __init__(self, name, colour, speed):
        self.name = name
        self.colour = colour
        self.speed = speed
        
    def honk(self):
        print("Honking...")
    
    def speedup(self, speed):
        self.speed += speed
    
    def speeddown(self, speed):
        if self.speed - speed < 0:
            print("Speed Can't be Negative")
            return
        
        self.speed-=speed
    
    def __repr__(self):
        return f"Name: {self.name}, Color: {self.colour}, Speed: {self.speed}"
    

class RaceCar(Car):
    
    def __init__(self, name, colour, speed):
        super().__init__(name, colour, speed)
        
    

nano_car = RaceCar("nano", "yellow", 0)
print(nano_car)
nano_car.speedup(20)
# nano_car.speedup()
print(nano_car)
nano_car.speeddown(10)
nano_car.speeddown(30)
print(nano_car)


