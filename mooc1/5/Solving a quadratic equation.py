from math import sqrt

# Get coefficients from the user
a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Calculate the two roots
root1 = (-b + sqrt(discriminant)) / (2 * a)
root2 = (-b - sqrt(discriminant)) / (2 * a)

# Display the result
print(f"The roots are {root1} and {root2}")
