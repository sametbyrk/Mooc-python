# Write your solution here
a1=float(input("Hourly wage: "))
a2=int(input("Hours worked: "))
a3=input("Day of the week: ")

if a3=="Sunday":
    print(f"Daily wages: {a1*a2*2} euros")
else:
    print(f"Daily wages: {a1*a2} euros")