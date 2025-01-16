num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))
choice = input("\n( Options + , - , * , / , % )\nEnter the operation : ")

if choice == '+':
    add = num1 + num2
    print(f"\n{num1} + {num2} = {add}")
elif choice == '-':
    sub = num1 - num2
    print(f"\n{num1} - {num2} = {sub}")
elif choice == '*':
    mul = num1 * num2
    print(f"\n{num1} * {num2} = {mul}")
elif choice == '/':
    try:
        div = num1 / num2
        print(f"\n{num1} / {num2} = {div}")
    except ZeroDivisionError as e :
        print("\nInvalid Division, Please Try again, Error : ",e)
elif choice == '%':
    perc = (num1 / num2)*100
    print(f"\n({num1} / {num2})*100 = {perc}%")
else:
    print(f"\nInvaild choice : {choice}")