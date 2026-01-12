#Take input from user

a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))

#Take operator from user to perform operation:

operator = input("Enter the operator(+, -, *, /):")

#if - elif - else condition to perform the calculations

if operator == "+" :
    print(a+b)
elif operator == "-" :
    print(a-b)
elif operator == "*" :
    print(a*b)
else:
    print(a/b)