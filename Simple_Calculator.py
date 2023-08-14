while True:
    print("Welcome to Calciii - Simple Calculator")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    chores = input("Select the Operation you want to do (1-5): ")

    if chores == '5':
        print("bye!")
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if chores == '1':
        result = num1 + num2
    elif chores == '2':
        result = num1 - num2
    elif chores == '3':
        result = num1 * num2
    elif chores == '4':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Cannot divide by zero.")
            continue
    else:
        print("Invalid. Please select a valid operation between 1-5.")
        continue

    print("Output:", result)
