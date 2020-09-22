def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    if y == 0:
        print("Invalid input")
    else:
        return x / y


while True:
    print("Select Operations")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Division")

    choice = input("Enter your choice")
    if choice == "Q" or choice == "q":
        break

    if choice == '1':
        num1 = float(input("Enter first number"))
        num2 = float(input("Enter second number"))
        print(add(num1, num2))

    elif choice == '2':
        num1 = float(input("Enter first number"))
        num2 = float(input("Enter second number"))
        print(num1, "-", num2, "=", sub(num1, num2))

    elif choice == '3':
        num1 = float(input("Enter first number"))
        num2 = float(input("Enter second number"))
        print(num1, "*", num2, "=", mul(num1, num2))

    elif choice == '4':
        num1 = float(input("Enter first number"))
        num2 = float(input("Enter second number"))
        print(num1, "/", num2, "=", div(num1, num2))

    else:
        print("Invalid Input")
