# Ask for three letters
letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

# Put the letters in a list and sort them
letters = [letter1, letter2, letter3]
letters.sort()

# Print the middle letter
middle_letter = letters[1]
print(f"The letter in the middle is {middle_letter}")
