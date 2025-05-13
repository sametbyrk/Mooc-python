# Write your solution here
s1=int(input("Please type in a temperature (F): "))
print(f"{s1} degrees Fahrenheit equals {(s1-32)/1.8} degrees Celsius")
if (s1-32)/1.8 <0:
    print("Brr! It's cold in here!")