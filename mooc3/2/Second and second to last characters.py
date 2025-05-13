text = input("Please type in a string: ")

# Check if the string is long enough to have a second and second-to-last character
if len(text) >= 2:
    if text[1] == text[-2]:
        print(f"The second and the second to last characters are {text[1]}")
    else:
        print("The second and the second to last characters are different")
else:
    print("The string is too short to compare the second and second to last characters.")
