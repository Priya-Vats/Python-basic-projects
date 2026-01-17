"""Grade System
Input marks (0 - 100)
Print grade:
90 - 100 → A
80 - 89 → B
70 - 79 → C
Else → Fail"""


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