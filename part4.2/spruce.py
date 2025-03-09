"""
Please write a function named spruce, which takes one argument.
The function prints out the text a spruce!, and the a spruce tree, the size of which is specified by the argument.
"""
def spruce(size):
    for i in range(size):
        stars = 2 * i + 1
        spaces = size - i - 1
        print(" " * spaces + "*" * stars)  #
    print(" " * (size - 1) + "*")

spruce(5)