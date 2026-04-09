balance = 1000

while True:
    print("\nWhat would you like to do?\n1. Check Balance\n2. Withdraw\n3. Exit")
    choice = input("Enter your choice: ").strip()


    def checkBal():
        print(f"Your current balance is: {balance:,.2f}")

    def withDraw():
            global balance
            print("\n      ----WITHDRAWING MONEY----")
            print(f"Your balance is: {balance:,.2f}")
            try:
                cash = float(input("Enter amount to withdraw: "))
                if balance < cash:
                        print("Insufficient funds.")
                else:
                    balance -= cash
                    print("\nWithdrawal succesful.")
                    print(f"Your new balance is: {balance:,.2f}")
                    return
            except ValueError:
                print("Invalid! Enter numbers only.")
                
        

    if choice == "1":
        checkBal()

    elif choice == "2":
        if balance == 0:
            print("There is no money to withdraw.")
        else:
            withDraw()

    elif choice == "3":
        print("Thank you for using our services.")
        break

    else:
        print("Invalid. Please select from choices only")
        continue
          
