from math import sqrt
def square_roots(numbers: list):
    return [sqrt(numb) for numb in numbers]

lines = square_roots([1, 2, 3, 4])
for line in lines:
    print(line)