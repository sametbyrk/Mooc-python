text = input("Please type in a string: ")
substring = input("Please type in a substring: ")

# Find the first occurrence of the substring
first_occurrence = text.find(substring)

# If the first occurrence is found, search for the second occurrence starting after the first occurrence
if first_occurrence != -1:
    second_occurrence = text.find(substring, first_occurrence + len(substring))

    if second_occurrence != -1:
        print(f"The second occurrence of the substring is at index {second_occurrence}.")
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur once in the string.")
