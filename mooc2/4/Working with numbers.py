# Initialize variables
count = 0
total_sum = 0
positive_count = 0
negative_count = 0

print("Please type in integer numbers. Type in 0 to finish.")

# Keep asking for numbers until the user types 0
while True:
    number = int(input("Number: "))

    if number == 0:
        break

    # Count numbers typed
    count += 1

    # Add the number to the total sum
    total_sum += number

    # Count positive and negative numbers
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1

# Calculate mean (avoid division by zero by ensuring at least one number was entered)
if count > 0:
    mean = total_sum / count
else:
    mean = 0  # To handle case if no number was entered, but this is not expected per the task

# Output the results
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {total_sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positive_count}")
print(f"Negative numbers {negative_count}")
