#Take input from user
num1 = int(input("Enter 1st no. :"))
num2 = int(input("Enter 2nd no. :"))
num3 = int(input("Enter 3rd no. :"))

#Print the greatest no. using if-elif-else
if num1>num2 and num1>num3:
    print("num1 is the greatest number")

elif num2>num1 and num2>num3:
    print("num2 is the greatest number")

else:
    print("num3 is the greatest number")