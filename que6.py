#1)	Write a python program to find whether a string is palindrome or not.

def is_palindrome(word):
    rev = word[::-1]
    return rev == word

if is_palindrome("malayalam"):
    print("It is a palindrome")

else:
    print("It is not a palindrome")

