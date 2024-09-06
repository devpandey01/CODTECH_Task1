def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choice = input("Enter choice: ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {num1 + num2}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {num1 - num2}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {num1 * num2}")
                elif choice == '4':
                    if num2 == 0:
                        print("Error! Division by zero.")
                    else:
                        print(f"{num1} / {num2} = {num1 / num2}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        else:
            print("Invalid choice. Please select a valid operation.")
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

calculator()
