"""
Please write a function named all_the_longest, which takes a list of strings as its argument.
The function should return a new list containing the longest string in the original list.
If more than one are equally long, the function should return all of the longest strings.
The order of the strings in the returned list should be the same as in the original.
"""


def all_the_longest(my_list):
    max_len = 0
    for string in my_list:
        if len(string) > max_len:
            max_len = len(string)

    longest_strings = []
    for string in my_list:
        if len(string) == max_len:
            longest_strings.append(string)

    return longest_strings

my_list = ["first", "second", "fourth", "eleventh"]
result = all_the_longest(my_list)
print(result)

