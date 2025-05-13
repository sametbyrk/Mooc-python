def print_many_times(text, times):
    # Print the text 'times' number of times
    for _ in range(times):
        print(text)

# testing the function:
print_many_times("hi", 5)
print()  # just to create a blank line between the outputs
text = "All Pythons, except one, grow up"
times = 3
print_many_times(text, times)
