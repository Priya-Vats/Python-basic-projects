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