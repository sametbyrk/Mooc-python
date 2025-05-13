limit = int(input("Limit: "))
total = 0
number = 1
numbers = []

while total < limit:
    total += number
    numbers.append(str(number))
    number += 1

calculation = " + ".join(numbers)
print(f"The consecutive sum: {calculation} = {total}")
