from math import sqrt

while True:
    # Ask for the number
    number = int(input("Please type in a number: "))

    # If the number is zero, exit the loop
    if number == 0:
        print("Exiting...")
        break

    # If the number is negative, print "Invalid number"
    elif number < 0:
        print("Invalid number")

    # If the number is positive, print its square root
    else:
        print(sqrt(number))