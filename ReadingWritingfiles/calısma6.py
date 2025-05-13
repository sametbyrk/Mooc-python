"""
with open("samet.txt") as new_file:
    contents = new_file.read()
    print(contents)

with open("samet.txt") as new_file:
    count = 0
    total_length = 0

    for line in new_file:
        line = line.replace("\n", "")
        count += 1
        print("Line", count, line)
        length = len(line)
        total_length += length

print("Total length of lines:", total_length)

def largest():
    with open("samet.txt") as new_file:
        first_line = new_file.readline()
        largest_number = int(first_line.replace("\n", ""))

        for line in new_file:
            line = line.replace("\n", "")
            number = int(line)
            if number > largest_number:
                largest_number = number

        return largest_number

print(largest())

text = "monkey,banana,harpsichord"
words = text.split(",")
for word in words:
    print(word)

#Virgülle ayrılmış Değerler
def read_fruits():
    fruits = {}
    with open("fruits.txt") as file:
        for line in file:
            line = line.strip()
            parts = line.split(";")
            fruit_name = parts[0]
            price = float(parts[1])
            fruits[fruit_name] = price
    return fruits

print(read_fruits())


def list_years(dates: list):
    year_list = []
    for date in dates:
        year_list.append(date[0])
    return year_list

date1 = (2019, 2, 3)
date2 = (2006, 10, 10)
date3 = (1993, 5, 9)

years = list_years([date1, date2, date3])
print(years)

class BankAccount:
    pass

peters_account = BankAccount()
peters_account.owner = "Peter Python"
peters_account.balance = 5.0

print(peters_account.owner)
print(peters_account.balance)

class BankAccount:

    # The constructor
    def __init__(self, balance: float, owner: str):
        self.balance = balance
        self.owner = owner


# constructor mantığı self this gibi
def  __init__(self,yaş:int,ad:str):
    self.yaş=yaş
    self.ad=ad

class Book:
    def __init__(self, name: str, author: str,genre :str,year:int):
        self.name = name
        self.author = author
        self.genre=genre
        self.year=year
python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)

print(f"{python.author}: {python.name} ({python.year})")
print(f"The genre of the book {everest.name} is {everest.genre}")

class Pet:
    def __init__(self, name: str, species: str, year_of_birth: int):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth
def new_pet(name: str, species: str, year_of_birth: int):
    object_pet =  Pet(name,species,year_of_birth)
    return object_pet

fluffy = new_pet("Fluffy", "dog", 2017)
print(fluffy.name)
print(fluffy.species)
print(fluffy.year_of_birth)

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

def older_book(book1: Book, book2: Book):
    if book1.year < book2.year:
        print(f"{book1.name} is older ({book1.year})")
    elif book1.year == book2.year:
        print(f"{book1.name} and {book2.name} are from the same year ({book1.year})")
    else:
        print(f"{book2.name} is older ({book2.year})")

python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

older_book(python, everest)
older_book(python, norma)


class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        self.value-=1
        if self.value<0:
            self.value=0

    #def increse(self,num:int):
      #  self.value +=num

counter = DecreasingCounter(10)
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.print_value()
"""
