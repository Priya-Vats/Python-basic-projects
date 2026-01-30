#Print numbers from 1 to 10 using for.

i = 0
for i in range(1,11) :
        print(i)

#Print numbers from 1 to 5 using while.
num = 1
while num <= 5:
    print(num)
    num += 1

#Print all even numbers from 1 to 20.
#Ist method
i = 0
for i in range(1,21):
    if i%2 == 0:
        print(i)
#2nd Method
for i in range(2,21,2):
    print(i)

#Stop printing when number becomes 5 (use break).
i = 1
while i <= 10:
    print(i)
    if (i==5):
        break
    i += 1

#Skip number 3 while printing 1 to 5 (use continue).
i = 1
while i <= 10: 
    if (i==3):
        i += 1
        continue
    print(i)
    i += 1
 