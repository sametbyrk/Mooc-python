number = int(input("Please type in a number: "))

# Loop through all numbers from 1 to the user input
for i in range(1, number + 1):
    for j in range(1, number + 1):
        print(f"{i} x {j} = {i * j}")
