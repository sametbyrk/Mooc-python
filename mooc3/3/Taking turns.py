number = int(input("Please type in a number: "))

# Define two pointers: one starting from the beginning (1), and one from the end (number)
start = 1
end = number

# Print the numbers alternating between the start and end until they meet
while start <= end:
    print(start)
    if start != end:
        print(end)
    start += 1
    end -= 1
