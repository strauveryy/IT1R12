while True:
    passWord = input("Enter your password 9 must contain atleast 1 letter and one number): ")
    letter = False
    number = False

    for char in passWord:
        if char.isalpha():
            letter = True
        elif char.isdigit():
            number = True
        
    if not  letter:
        print("Invalid Password! Must contain letter annumber")
    elif not number:
        print("Invalid Password! Must contain letter and number")
    else:
        print("Password Accepted")
        break
