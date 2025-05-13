text = input("Please type in a string: ")

# Check for each vowel and print whether it's found or not
for vowel in ['a', 'e', 'o']:
    if vowel in text:
        print(f"{vowel} found")
    else:
        print(f"{vowel} not found")
