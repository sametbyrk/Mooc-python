"""
Please write a function named mean, which takes a list of integers as an argument.
 The function returns the arithmetic mean of the values in the list.
"""
my_list = [1, 2, 3, 4, 5]

def mean(lst):

   return sum(lst)/len(lst)

my_list = [1, 2, 3, 4, 5]
result = mean(my_list)
print("mean value is", result)