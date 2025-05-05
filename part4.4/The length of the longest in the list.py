"""
Please write a function named length_of_longest, which takes a list of strings as its argument.
The function returns the length of the longest string.
"""
def length_of_longest(my_list):
    best = len(my_list[0])
    for i in my_list:
        if len(i)>best:
            best=len(i)
    return best

my_list = ["first", "second", "fourth", "eleventh"]
result = length_of_longest(my_list)
print(result)