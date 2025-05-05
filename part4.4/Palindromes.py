"""
Please write a function named palindromes, which takes a string argument and returns True if the string is a palindrome.
Palindromes are words which are spelled exactly the same backwards and forwards.
"""
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("kayak"))
print(is_palindrome("python"))
print(is_palindrome("madam"))