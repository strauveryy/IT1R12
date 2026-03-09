userInput = []


while True:
   print("MAIN MENU:\n1)Show Users \n2)Add User \n3)Update User \n4)Delete User \n5)Exit")

   choice = int(input("Enter your choice: ")) 

   if choice == 1:
        if userInput == []:
         print("\nNo users yet!")
        else:
         print("Users:")
         for idx, user in enumerate(userInput, 1):
             print(idx,userInput)

   elif choice == 2:
        name = input("\nEnter name: ")
        age = int(input("Enter age: "))
        userInput.append(f"{name} - {age}")
        print("User added successfully.")

   elif choice == 3:
        index = int(input("\nEnter the index of the user to update: "))
        if 0 <= index < len(userInput):
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            userInput[index] = f"{name} - {age}"
            print("User updated successfully.")
        else:
            print("\nInvalid index.")
            
   elif choice == 4:
        index = int(input("\nEnter the index of the user to delete: "))
        if 0 <= index < len(userInput):
            del userInput[index]
            print("User deleted successfully.")
        else:
            print("\nInvalid index.")
    
   elif choice == 5:
       print("\nThank you for using our program!")
       exit(0)

   else:
        print("\nInvalid choice. Please try again.")
        print("\nMAIN MENU:\n1)Show Users \n2)Add User \n3)Update User \n4)Delete User \n5)Exit")
        choice = int(input("Enter your choice: "))
