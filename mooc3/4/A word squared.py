def squared(word, size):
    # Loop to print each row
    for i in range(size):
        # For each row, create the string by shifting the word appropriately
        row = ""
        for j in range(size):
            row += word[(i + j) % len(word)]
        print(row)

# testing the function:
squared("ab", 3)
print()  # blank line between the outputs
squared("aybabtu", 5)
