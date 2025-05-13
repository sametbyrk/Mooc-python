word = input("Please type in a word: ")
char = input("Please type in a character: ")

# Find the first occurrence of the character
index = word.find(char)

# Check if the character is found and there are at least 3 characters from it
if index != -1 and index + 3 <= len(word):
    print(word[index:index+3])
