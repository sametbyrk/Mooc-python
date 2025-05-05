"""
Please write a function named shortest, which takes a list of strings as its argument.
The function returns whichever of the strings is the shortest.
If more than one are equally short, the function can return any of the shortest strings (there will be no such situation in the tests).
You may assume there will be no empty strings in the list.
"""
def shortest(my_list):
    shortest_str = my_list[0]
    for i in my_list:
        if len(i) < len(shortest_str):
            shortest_str = i
    return shortest_str

my_list = ["first", "second", "fourth", "eleventh"]
result = shortest(my_list)
print(result)
