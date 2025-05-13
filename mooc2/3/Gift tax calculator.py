# Ask for the value of the gift
gift_value = float(input("Value of gift: "))

# Calculate the tax based on the gift value
if gift_value < 5000:
    print("No tax!")
elif 5000 <= gift_value < 25000:
    tax = 100 + (gift_value - 5000) * 0.08
    print(f"Amount of tax: {tax:.1f} euros")
elif 25000 <= gift_value < 55000:
    tax = 1700 + (gift_value - 25000) * 0.10
    print(f"Amount of tax: {tax:.1f} euros")
elif 55000 <= gift_value < 200000:
    tax = 4700 + (gift_value - 55000) * 0.12
    print(f"Amount of tax: {tax:.1f} euros")
elif 200000 <= gift_value < 1000000:
    tax = 22100 + (gift_value - 200000) * 0.15
    print(f"Amount of tax: {tax:.1f} euros")
else:
    tax = 142100 + (gift_value - 1000000) * 0.17
    print(f"Amount of tax: {tax:.1f} euros")
