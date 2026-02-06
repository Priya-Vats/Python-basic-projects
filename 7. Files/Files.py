#Create a file and write: Hello File
f = open("7. Files/create.txt", "w")
f.write("Hello File")
f.close()

#Add changes in the create.txt file
f = open("7. Files/create.txt", "a")
f.write("\nI am New File and The name of the file is Create.txt")
f.close()

#Read the file and print its content.
f = open("7. Files/create.txt", "rt")
data = f.read()
print(data)

#Write Multiple lines into a file.
f = open("7. Files/create.txt", "a")
f.write("\nIt is feeling good to back. \nI am learning more new concept. \nNow I will Also Focus and learn C++ for my college requirements.")
f.close()

#Read file and count lines

f = open("7. Files/create.txt", "rt")
count = 0
for line in f:
    print(line, end="")
    count += 1
print("\nNumber of lines: ", count)
f.close()

#Append new text to exixting file.
f = open("7. Files/create.txt", "a")
f.write("\nI am back with some new learnings and Happy to share it with myself.")
f.write("\nAnd This time I must say I am better then my last self.")
f.write("\nAlso ready to change myself more and make my learnings to next level.")
f.write("\nSEE YOU SOON guys, ByY")
f.close()



#Copy content from one file to another.
file1 = open("7. Files/create.txt", "r")
content = file1.read()
file1.close()

file2 = open("7. Files/copy.txt", "w")
file2.write(content)
file2.close()

print("Content copied successfully")

#Another method using loop
file1 = open("7. Files/create.txt", "r")
file2 = open("7. Files/copy.txt", "w")

for line in file1:
    file2.write(line)

file1.close()
file2.close()

print("Content copied successfully")

#Another method using "with"
with open("7. Files/create.txt", "r") as file1:
    with open("7. Files/copy.txt", "w") as file2:
        file2.write(file1.read())