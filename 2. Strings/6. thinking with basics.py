#Count how many times letter "a" appears in a string.
word = input("Enter the word: ")
count = word.count('a')
print(count)

#Print only vowels from a string.
word = input("Enter the word: ")
word = word.lower()
for ch in word:
    if ch in "aeiou":
        print(ch)

#Replace all spaces in a string with _.
n = input("Enter the word: ")
n = n.replace(" ", "_")
print(n)

#Check if a string starts with "P".
ch = input("Enter the word: ")
if ch[0] == "P":
    print("Starts with P")
else:
    print("Does not start with P")

#Print characters at even index positions.
ch = input("Enter the word: ")
for i in range(len(ch)):
    if i%2 == 0:
        print(ch[i])