#Function to check: Even or Odd

def check_even_odd(num):
    if num%2 == 0:
        print("Even")
    else:
        print("Odd")

number = int(input("Enter the Number:"))
check_even_odd(number)

#Function to find : Square of number
def square_of_number(num):
    print(num*num)

num = int(input("Enter the Number:"))
square_of_number(num)

#Function that returns:  largest of two numbers      
def largest(a,b):
    if a>b:
        print("A is the largest number")
    else:
        print("B is the largest number")

A = float(input("Enter the number A"))
B = float(input("Enter the number B"))

largest(A, B)

#Function that prints numbers from 1 to n.
def num(n):
    for i in range(1,n+1):
        print(i)
        #i += 1

a = int(input("Enter the number:"))
num(a)

#Function that counts vowels in string.
def count_vowels(word):
    count = 0
    for ch in word:
        if ch in "aeiou":
            count += 1
    return count

word = input("Enter the word:")
result = count_vowels(word)
print(result)

        