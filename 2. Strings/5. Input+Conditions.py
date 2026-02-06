#Take a number:Print "Small" if < 10, Print "Medium" if 10–50, Print "Large" if > 50

n = float(input("Enter the number:"))
if n <10:
    print("Small")
elif n >= 10 and n <= 50:
    print("Medium")
else:
    print("Large")

#Take 3 numbers: Print smallest number

a = float(input("Enter the number:"))
b = float(input("Enter the number:"))
c = float(input("Enter the number:"))

if a<b and a<c:
    print("Smallest Number is:" , a)
elif b<a and b<c:
    print("Smallest Number is:" , b)
else:
    print("Smallest Number is:" , c)

#Take a character: Check if it’s a vowel or consonant

ch = input("Enter a character:")
ch = ch.lower()
if ch in "aeiou":
    print("The character is Vowel.")
else:
    print("The character is Constant")

#Take username & password: If username = "admin" and password = "1234" → Login successful
user = input("Enter the Username: ")
password = int(input("Enter the Password"))

if user == "admin" and password == 1234:
    print("Login Successful")
elif user == "admin" and password != 1234:
    print("Wrong Password!!")
elif user != "admin" and password == 1234:
    print("Wrong Username!!")
else:
    print("Try Again!!!")


#Take age and gender: If age ≥ 18 → Eligible , Else → Not eligible
age = float(input("Enter your age:"))

if age>= 18:
    print("Eligible")
else:
    print("Not Eligible")