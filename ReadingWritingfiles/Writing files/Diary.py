while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    command = input("Function: ")

    if command == "0":
        print("Bye now!")
        break

    elif command == "1":
        entry = input("Diary entry: ")
        with open("diary.txt", "a") as file:
            file.write(entry + "\n")
        print("Diary saved")

    elif command == "2":
        print("Entries:")
        try:
            with open("diary.txt", "r") as file:
                content = file.read()
                print(content.strip())  # sadece sonunda boş satır varsa onu temizlemek için
        except FileNotFoundError:
            print("No entries yet.")
