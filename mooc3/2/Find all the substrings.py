word = input("Please type in a word: ")
char = input("Please type in a character: ")

# Loop through the string to find substrings
for i in range(len(word)):
    # Check if the substring starts with the specified character and has at least 3 characters
    if word[i] == char and i + 3 <= len(word):
        print(word[i:i+3])
