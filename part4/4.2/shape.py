"""
Please write a function named shape, which takes four arguments.
The first two parameters specify a triangle, as above, and the character used to draw it.
The first parameter also specifies the width of a rectangle, while the third parameter specifies its height.
The fourth parameter specifies the filler character of the rectangle.
The function prints first the triangle, and then the rectangle below it.
The function should call the function line from the exercise above for the actual printing out.
Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.
"""
def shape(width,character,height,string):
    for i in range(1,height+1):
        print(character * i)

    for a in range(width):
        print(height*string)

shape(5, "X", 3, "*")
print()
shape(2, "o", 4, "+")
print()
shape(3, ".", 0, ",")