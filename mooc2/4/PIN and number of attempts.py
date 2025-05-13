# Correct PIN code
correct_pin = "4321"

# Initialize attempt counter
attempts = 0

while True:
    # Ask for the PIN
    pin = input("PIN: ")
    attempts += 1

    # Check if the PIN is correct
    if pin == correct_pin:
        if attempts == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {attempts} attempts")
        break
    else:
        print("Wrong")
