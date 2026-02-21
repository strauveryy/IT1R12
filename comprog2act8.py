def myFunc():
    if choiceNi == 1:
        add = float(firstNum + secondNum)
        print(f"{firstNum} + {secondNum} =", add)
    elif choiceNi == 2:
        subtract = float(firstNum - secondNum)
        print(f"{firstNum} - {secondNum} =", subtract)
    elif choiceNi == 3:
        multiplication = float(firstNum * secondNum)
        print(f"{firstNum} * {secondNum} =", multiplication)
    elif choiceNi == 4:
        division = float(firstNum / secondNum)
        print(f"{firstNum} / {secondNum} =", division)
    else:
        print("Invalid")

print ("SELECT OPERATION.")
print("1.Add\n2.Subtract \n3.Multiply \n4.Divide")

choiceNi = int(input("Enter choice(1/2/3/4): "))
firstNum = float(input("Enter first number: "))
secondNum = float(input("Enter second number: "))


myFunc()
