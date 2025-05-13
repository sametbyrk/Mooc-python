word = input("Word: ")

# Calculate the number of spaces needed for centering
spaces_needed = 30 - len(word) - 2  # Subtract 2 for the '*' characters on either side

# Print the top border of the frame
print("*" * 30)

# Print the middle line with the word centered
print("*" + " " * (spaces_needed // 2) + word + " " * (spaces_needed - spaces_needed // 2) + "*")

# Print the bottom border of the frame
print("*" * 30)
