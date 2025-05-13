text = input("Please type in a string: ")

# Print all substrings starting from the first character
for i in range(1, len(text) + 1):
    print(text[:i])
