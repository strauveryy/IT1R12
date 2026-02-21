def cloSest():
    print("Find the closest number to 300")
    numA = input("Enter your first number: ")
    numB = input("Enter your second number: ")
    numC = input("Enter your third number: ")

    largest = max(numA, numB, numC)
    lowest = min(numA, numB, numC)
    print(lowest)
    print(largest)
    numNisya = int(largest)
    numNisya2 = int(lowest)

    if  numNisya < x:
        print(f"{largest} is the number closest to 300")
    elif numNisya2 > x:
        print(f"{lowest} is the number closest to 300")
    else: 
        print("Invalid")
       

x = 300

cloSest()
