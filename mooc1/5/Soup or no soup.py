# Write your solution here
isim=input("Please tell me your name: ")
if isim != "Jerry":
    adet=int(input("How many portions of soup? "))
    print(f"The total cost is {adet*5.90}")
    print("Next please!")
else:
    print("Next please!")