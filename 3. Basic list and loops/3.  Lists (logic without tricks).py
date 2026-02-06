#Count how many numbers are even in a list.
num = [1,2,3,4,5,6,7,8,9,10]
count = 0
for n in num:
    if n % 2 == 0:
        print(n)
        count += 1
print(count)

#Find the sum of odd numbers in a list.        

num = [1,2,3,4,5,6,7,8,9,10]
count = 0
for n in num:
    if n % 2 != 0:
        count = count + n
print(count)

#Create a new list containing only numbers > 10
num = [12, 32, 15, 7, 9, 19, 1, 24]
new_list = []
for i in num:
    if i > 10:
        new_list.append(i)
print(new_list)

#Reverse a list using a loop (no reverse()).

new = ["letter", "teller", "author", "poetry", "listener"]
rev_new = []
for i in range(len(new) -1,-1,-1):
    rev_new.append(new[i])
print(rev_new)

#Check if a number exists in a list.

num = [5,8,9,5,7,1]
n = float(input("Enter the number: "))

if n in num:
    print("Found")
else:
    print("Not Found")