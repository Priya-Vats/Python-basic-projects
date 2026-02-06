#Write a function that prints:
def Print_word():
    #print("hello")
    return "hello"

output = Print_word()
print(output)

#Write a function that takes a name and prints it.

name = input("Enter the name: ")
def Letter(name):
    #print("name")
    return name

output = Letter(name)
print(output)
#print(name())

#Write a function that returns the sum of two numbers.
a = float(input("Enter the number:"))
b =  float(input("Enter the number:"))
def sum(a,b):
    S = a+b
    return S

print(sum(a,b))

#Write a function with a default parameter.
#Ist method
def greet(name = "User"):
    #name = "Priya"
    print("Hello",  name)
    return greet

print(greet(name = "user"))

#2nd method and better method
def greet(name = "user"):
    print("Hello", name)

#greet()
greet("Priya")
