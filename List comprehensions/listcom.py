"""

class LotteryNumbers:
    def __init__(self, week: int, numbers: list):
        self.week = week
        self.numbers = numbers

    def number_of_hits(self, numbers: list):
        return len([number for number in numbers if number in self.numbers])

    def hits_in_place(self,numbers:list):
        return [number if number in numbers else -1 for number in self.numbers]

week5 = LotteryNumbers(5, [1, 2, 3, 4, 5, 6, 7])
my_numbers = [1, 4, 7, 11, 13, 19, 24]
print(week5.number_of_hits(my_numbers))

week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
my_numbers = [1,4,7,10,11,20,30]

print(week8.hits_in_place(my_numbers))


test_string = "Hello there, this is a test!"

vowel_string = "".join([character for character in test_string if character in "aeiou"])

print(vowel_string)

def filter_forbidden(string: str, forbidden: str):
     return "".join([word for word in string if word not in forbidden])
sentence = "Once! upon, a time: there was a python!??!?!"
filtered = filter_forbidden(sentence, "!?:,.")
print(filtered)


sentence = "hello there"

char_counts = {character : sentence.count(character) for character in sentence}
print(char_counts)

def lengths(strings: list):
    return   {string : len(string) for string in strings}
word_list = ["once", "upon" , "a", "time", "in"]

word_lengths = lengths(word_list)
print(word_lengths)

from fileinput import filename


def most_common_words(filename: str, lower_limit):
    with open(filename) as file:
        return [{filename:lower_limit for line in filename if lower_limit>3}]


def add_numbers_to_list(numbers: list):
   if len(numbers)%5 !=0:
    numbers.append(numbers[len(numbers)-1]+1)
    add_numbers_to_list(numbers)

numbers = [1, 3, 4, 5, 10, 11]
add_numbers_to_list(numbers)
print(numbers)

print("----------------------------------part 4 kodlar"----------------------------------------------)
def mach(mylist:list,aranan:int):
    count=0
    for row in mylist:
        for item in row:
            if item==aranan:
                count +=1
    return count

aranan_sayi = 1
count = mach([[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]], aranan_sayi)
print(f"'{aranan_sayi}' sayısı listede {count} kez tekrar etti.")
"""
def uzun(mylist:list):
    max=""
    for kelime in mylist:
        if len(kelime)>len(max):
            max=kelime
    return max
enuzunstring = uzun(["hi", "hiya", "hello", "howdydoody", "hi there"])
print(enuzunstring)
