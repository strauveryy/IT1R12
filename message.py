try:

    with open("message.txt", "x") as file:
        print("File Created succesfully")

except FileExistsError:
    print("File already exists")


def sendMessage():
    try: 
        message = input("Enter message: ")

        with open("message.txt", "a") as file:
            file.write(f"\n{message}")

    except ValueError:
        print("Invalid. Try again")

def viewMessage():
    try:
        with open("message.txt", "r") as file:
            messijs = file.readlines()

        if not messijs:
            print("File is empty")

        print("=== MESSAGES ===")
        for messij in messijs:
            print(messij)
        print()

    except FileNotFoundError:
        print("file does not exist.")

def mainMenu():
    while True:
        print("\n==SELECT OPTION==")
        print("1. Send Message \n2. View Messages \n3. Exit Program")
        choice = input("Enter choice: ")

        if choice == "1":
            sendMessage()

        elif choice == "2":
            viewMessage()

        elif choice == "3":
            print("Thank you for using our program.")
            break

        else:
            print("Invalid input. Please select from choices")

mainMenu()

