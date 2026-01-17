"""Count Vowels & Consonants

Input a string

Count vowels and consonants separately"""

import random
import string

words = input("enter the word:")

str1 = ('a', 'e', 'i', 'o', 'u')
str2 = string.ascii_letters - str1

print(str.count(str1))
print(str.count(str2))