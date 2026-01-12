#Take input from user
marks = float(input("Enter marks:"))

#Print Grades using if-elif-else

if marks >=90:
    print("A")

elif marks>=80 and marks<90:
    print("B")

elif marks>=70 and marks<80:
    print("C")

else:
    print("D")