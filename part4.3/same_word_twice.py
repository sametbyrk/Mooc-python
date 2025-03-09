"""
Please write a program which asks the user for words.
If the user types in a word for the second time,
the program should print out the number of different words typed in, and exit.
"""
words = []
while True:
    word = input("word :")
    if word in words:
        print(f"You typed in {len(set(words))} different words")
        break
    else:
        words.append(word)

