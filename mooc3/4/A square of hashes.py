def hash_square(length):
    # Print the square by repeating the hash string 'length' times
    for _ in range(length):
        print('#' * length)

# testing the function:
hash_square(3)
print()  # just to create a blank line between the outputs
hash_square(5)
