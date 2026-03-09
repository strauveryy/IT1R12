class shopPing:
    def __init__(self):
        self.Cart = []

    def addCart(self):
        item = input("Add item name: ")
        self.Cart.append(item)
        print(f"{item} added to cart.")

    def removeCart(self):
        index = int(input("Enter item to remove: "))
        if 1 <= index <= len(self.Cart):       
            removed = self.Cart[index - 1]        
            self.Cart.pop(index - 1)
            print(f"\n{removed} removed from cart.")
        else:
            print("Item not found !!")

    def viewCart(self):
        if self.Cart == []:
            print("\nNo ITEMS ADDED IN CART YET.")
        else: 
            print("\nCART:")
            for idx, item in enumerate(self.Cart, 1):   
                print(f"{idx}.) {item}")

    def checkoutCart(self):
        if self.Cart == []:
            print("\nNo items in cart!")
            print("1. Go back to menu")
            print("2. Exit mall")
            option = int(input("Choose option: "))
            if option == 1:
                return                  
            elif option == 2:
                print("Thank you for visiting Auvrey's Shopping Mall!")
                exit(0)
            else:
                print("Invalid choice, going back to menu.")
                return
        else:
            print("\nChecking out...")
            print("Items purchased:")
            for idx, item in enumerate(self.Cart, 1): 
                    print(f"{idx}.) {item}")
            print("\nThank you for shopping!")
            exit(0)
            
cart = shopPing()

while True:
    print("\nWelcome to Auvrey's Shopping Mall!")
    print("1.) Add Item \n2.) Remove Item \n3.) View Cart \n4.) Checkout")
    
    choice = int(input("Choose option: "))

    if choice == 1:
        cart.addCart()
    elif choice == 2:
        cart.removeCart()        
    elif choice == 3:
        cart.viewCart()
    elif choice == 4:
        cart.checkoutCart()
    else:
        print("Invalid choice!")
