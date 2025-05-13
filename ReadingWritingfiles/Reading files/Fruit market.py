def read_fruits():
    result = {}
    file = open("fruits.csv", "r")
    for line in file:
        name, price = line.strip().split(";")
        result[name] = float(price)
    return result
