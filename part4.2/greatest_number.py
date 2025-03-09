"""
Please write a function named greatest_number, which takes three arguments.
The function returns the greatest in value of the three.
"""
def greatest_number(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(f"{num1} büyüktür")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} büyüktür")
    else:
        print(f"{num3} büyüktür")

greatest_number(5,6,8)

