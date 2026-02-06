#Create a dictionary of 3 students with marks.
#Print student name if marks > 80

marks = {
    "Arjun" : 87,
    "Karan" : 79,
    "Ishaan": 90,
}

for i in marks:
    if marks[i] > 80:
        print(i)

#Count total number of keys in dictionary.
marks = {
    "Arjun" : 87,
    "Karan" : 79,
    "Ishaan": 90,
}
#print(len(marks))

count = 0
for key in marks:
    count = count+1
print(count)

#Check if a key exists in dictionary.
info = {
    "name" : "Ishaan",
    "age" : 21,
    "marks": 90,
}

n = input("Enter the key:")
if n in info:
    print("Key Exits")
else:
    print("Key do not Exist")


#Add a new key-value pair.
info = {
    "name" : "Ishaan",
    "age" : 21,
    "marks": 90,
}

info.update({"car" : "Mercedes"})
print(info)

#Print dictionary in this format: 
#name : Rahul
#age  : 20
info = {
    "name" : "Ishaan",
    "age" : 21,
    "marks": 90,
}

for key in info:
    print(key, ":", info[key])
