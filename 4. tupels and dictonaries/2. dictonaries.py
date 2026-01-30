#Create a dictionary with: name, age, city and Print all values.

Biodata = { 
    "name" : "Ishan",
    "Age" : 23,
    "city" : "Banglore",
    }

print(Biodata)

#Print only the keys of a dictionary.

print(Biodata.keys())

#Update the age in the dictionary.

Biodata.update({"Age" : 24})
print(Biodata)