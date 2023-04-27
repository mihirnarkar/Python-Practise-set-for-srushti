'''
Q.2) WAP to find if the given word is a keyword or not 

Case1:
Input: New
Output: New is not a keyword

Case2:
Input: While
Output: While is a keyword
'''

import keyword

word = input("Enter word: ")

if keyword.iskeyword(word):
    print(f"{word} is a keyword")
else:
    print(f"{word} is not a keyword")