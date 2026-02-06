#Class Car: attributes = brand and model. And Method = display info

class Car:
    wheels = 4 #--> Class Variable
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print("Brand Name:", self.brand, Car.wheels)
        print("Model:", self.model, Car.wheels)

car = Car("Mercedes", "Mercedes Benz Group AG.")
car.display_info()

#Constructor that accepts values.
class Objects:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
s1 = Objects("Anuraag\n",72)
s2 = Objects("Anamika", 85)

print(s1.name, s1.roll)

