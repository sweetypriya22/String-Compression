'''
Write a Python program that checks whether a given string is a palindrome.



A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.



The program must ignore the following when checking for a palindrome:

Spaces
Punctuation (like commas, periods, exclamation marks)
Case (uppercase vs. lowercase letters)


Input Format:

A string 's' that may contain letters, spaces, and punctuation.
'''
a = input()
def is_palindrome(a):
    New = ""
    s = a.lower()
    for i in s:
        if i.isalnum():
            New+=i
    return New == New[::-1]
            
        
          
print(is_palindrome(a))