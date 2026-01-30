#Take a string and check:Does it contain the letter "a"?

word = input("Enter the sentence:")

if 'a' in word:
    print("it contain")
else:
    print("does Not contain")

#Take a string and print it without spaces.
word = input("Enter the sentence:")
print(word.replace(" ",""))