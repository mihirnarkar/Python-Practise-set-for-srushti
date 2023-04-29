# Q.8) Pallindrome code in python:-

def isPallindrome(word):
    return word == word[::-1]

word = input("Enter word: ")
print(f"Given word, {word} is a {isPallindrome(word)}")