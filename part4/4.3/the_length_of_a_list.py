"""
Please write a function named length which takes a list as its argument and returns the length of the list.
"""
def length(lst):
    count = 0
    for item in lst:
        count += 1
    return count

my_list = [1, 2, 3, 4, 5]
result = length(my_list)
print("The length is", result)

result = length([1, 1, 1, 1])
print("The length is", result)
