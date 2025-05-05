"""
Please write a function named same_chars, which takes one string and two integers as arguments.
The integers refer to indexes within the string.
The function should return True if the two characters at the indexes specified are the same.
Otherwise, and especially if either of the indexes falls outside the scope of the string, the function returns False.
"""
def same_chars(word,num1,num2):
    if word[num1] == word[num2]:
        print("true")
    else:
        print("false")

same_chars("simit",2,3)