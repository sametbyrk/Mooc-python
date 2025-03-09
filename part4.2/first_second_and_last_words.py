"""
Please write three functions: first_word, second_word and last_word. Each function takes a string argument.
As their names imply, the functions return either the first, the second or the last word in the sentence they receive as their string argument.
In each case you may assume the argument string contains at least two separate words, and all words are separated by exactly one space character.
There will be no spaces in the beginning or at the end of the argument strings.
"""
def first_word(sentence):
    space_index = sentence.find(" ")
    return sentence[:space_index]

def second_word(sentence):
    first_space = sentence.find(" ")
    second_space = sentence.find(" ", first_space + 1)
    return sentence[first_space + 1:second_space]

def last_word(sentence):
    last_space = sentence.rfind(" ")
    return sentence[last_space + 1:]


sentence = "rüzgar efe bayrak"

print(first_word(sentence))
print(second_word(sentence))
print(last_word(sentence))