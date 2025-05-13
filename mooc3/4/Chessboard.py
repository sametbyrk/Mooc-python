def chessboard(length):
    # Loop through each row
    for i in range(length):
        # For each row, we alternate between starting with '1' or '0'
        row = ""
        for j in range(length):
            if (i + j) % 2 == 0:
                row += "1"
            else:
                row += "0"
        print(row)

# testing the function:
chessboard(3)
print()  # blank line between the outputs
chessboard(6)
