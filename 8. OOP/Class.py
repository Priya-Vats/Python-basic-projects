"""#Create a class Student with: name, roll number, Print details using a method.
class Student:
    def __init__(self, name, rollnumber):
        self.name = name
        self.roll = rollnumber

    def display(self):
        print("name: ", self.name)
        print("roll number: ", self.roll)

s1 = Student("Priya Vats", 114)
s1.display()
#print(s1.name, s1.roll)

#Create a constructor that prints: Student created

class Message:
    def __init__(self, message):
        self.message = message

    def display(self):
        print("Update:", self.message)
    

m1 = Message("Student Created")
m1.display()
#print(m1.message)""" 


#Create two objects of the class.
class Objects:
    def __init__(self, cars, brand):
        self.car = cars
        self.brand = brand
    
    def display(self):
        print("Name:", self.car)
        print("Brand:", self.brand)

c1 =  Objects("Mercedes", "Mercedes-Benz Group AG.")
c1.display()
#print(c1.car, c1.brand)

c2 = Objects("Defender" , "Land Rover")
c2.display()
#print(c2.car, c2.brand)

