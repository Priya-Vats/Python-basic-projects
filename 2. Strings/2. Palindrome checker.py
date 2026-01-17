"""Palindrome Checker
Check if a string is palindrome"""

#Take the input from user

word = input("enter the word:")

#use loop to print the result
if word == word [::-1]:
    print("Palindrome")

else:
    print("Not Palindrome")