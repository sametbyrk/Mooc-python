while True:
    text = input("Please type in a string: ")

    # If the input is empty, break the loop
    if text == "":
        break

    # Print the string and its underline
    print(text)
    print("-" * len(text))
