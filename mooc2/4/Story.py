# Write your solution here
cumle=""
kontrol=""
while True:
    kelime = input("Please type in a word: ")
    if kontrol==kelime:
        break
    kontrol = kelime
    cumle +=kelime

print(cumle)
