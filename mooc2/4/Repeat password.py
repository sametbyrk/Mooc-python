# Ask for the initial password
password = input("Password: ")

# Loop until the user types the same password again
while True:
    repeat_password = input("Repeat password: ")

    if repeat_password == password:
        print("User account created!")
        break
    else:
        print("They do not match!")
