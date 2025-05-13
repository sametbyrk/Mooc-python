number = int(input("Please type in a number: "))

# Loop through numbers from 1 to the input number
for i in range(1, number, 2):
    # Print the pair in reversed order
    print(i + 1)
    print(i)

# If the number is odd, print the last number
if number % 2 != 0:
    print(number)
