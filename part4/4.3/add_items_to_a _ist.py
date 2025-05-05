"""
Please write a program which first asks the user for the number of items to be added.
Then the program should ask for the given number of values,
one by one, and add them to a list in the order they were typed in.
Finally, the list is printed out.
"""
items = int(input("How many items: "))

liste = []
for i in range(items):
    number = int(input(f"sayı gir :"))
    liste.append(number)

print(liste)