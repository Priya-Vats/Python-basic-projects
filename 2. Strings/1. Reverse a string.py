"""Reverse a String
Input a string
Print it reversed (without using built-in reverse)"""

#Take the input from user
s = input("enter a word:")

#Print the word in reverse order for ex = "Hello" -> "olleh"
reversed_str = ""

for i in range(len(s)-1, -1, -1):
    reversed_str += s[i]
    
print(reversed_str)

    