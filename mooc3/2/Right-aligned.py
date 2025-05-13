text = input("Please type in a string: ")

# Calculate how many '*' characters are needed
stars_needed = 20 - len(text)

# If the string is shorter than 20 characters, add '*' at the beginning
if stars_needed > 0:
    text = '*' * stars_needed + text

# Print the resulting string
print(text)
