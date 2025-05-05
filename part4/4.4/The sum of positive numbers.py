"""
Please write a function named sum_of_positives, which takes a list of integers as its argument.
The function returns the sum of the positive values in the list.
"""
def sum_of_positives(arr):
    total = 0
    for num in arr:
        if num > 0:
            total += num
    return total

my_list = [1, -2, 3, -4, 5]
result = sum_of_positives(my_list)
print("The result is", result)