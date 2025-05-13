def is_leap_year(year):
    # A year is a leap year if:
    # - It is divisible by 4, and
    # - If it is divisible by 100, it must also be divisible by 400
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

# Ask for the input year
year = int(input("Year: "))

# Find the next leap year
next_year = year + 1

# Loop until we find the next leap year
while not is_leap_year(next_year):
    next_year += 1

# Print the result
print(f"The next leap year after {year} is {next_year}")
