"""
Please write a program which asks the user to type in values and adds them to a list.
After each addition, the list is printed out in two different ways:

in the order the items were added
ordered from smallest to greatest
The program exits when the user types in 0.
"""
list = []
while True:
    item = int(input("New item :"))
    if item == 0:
        print("bye")
        break

    list.append(item)

    print(f"{list} now")
    print(sorted(list))