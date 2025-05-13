# Write your solution here
a1=int(input("How many times a week do you eat at the student cafeteria? "))
a2=float(input("he price of a typical student lunch? "))
a3=float(input("How much money do you spend on groceries in a week? "))
print("Average food expenditure:")
b=(a2*a1+a3)/7
print(f"Daily: {b} euros")
print(f"Weekly: {a2*a1+a3} euros")