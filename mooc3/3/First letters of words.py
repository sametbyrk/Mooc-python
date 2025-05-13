sentence = input("Please type in a sentence: ")

# Split the sentence into words
words = sentence.split()

# Print the first letter of each word
for word in words:
    print(word[0])
