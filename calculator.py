#Calculator
# ==========================================
#       MULTI-NUMBER CALCULATOR
# ==========================================

history = []


def get_numbers():
    while True:
        try:
            n = int(input("\nHow many numbers do you want to enter? "))

            if n < 1:
                print("Please enter at least 1 number.")
                continue

            numbers = []

            for i in range(n):
                while True:
                    try:
                        num = float(input(f"Enter number {i + 1}: "))
                        numbers.append(num)
                        break
                    except ValueError:
                        print("Invalid input! Please enter a number.")

            return numbers

        except ValueError:
            print("Please enter a valid whole number.")


def addition(numbers):
    return sum(numbers)


def subtraction(numbers):
    result = numbers[0]

    for num in numbers[1:]:
        result -= num

    return result


def multiplication(numbers):
    result = 1

    for num in numbers:
        result *= num

    return result


def division(numbers):
    result = numbers[0]

    for num in numbers[1:]:
        if num == 0:
            return None

        result /= num

    return result


def modulus(numbers):
    result = numbers[0]

    for num in numbers[1:]:
        if num == 0:
            return None

        result %= num

    return result


def power(numbers):
    result = numbers[0]

    for num in numbers[1:]:
        result **= num

    return result


def show_menu():
    print("\n================================")
    print("       MULTI-NUMBER CALCULATOR")
    print("================================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Average")
    print("8. Maximum")
    print("9. Minimum")
    print("10. Calculation History")
    print("0. Exit")
    print("================================")


while True:

    show_menu()

    choice = input("Enter your choice: ")

    if choice == "0":
        print("\nThank you for using the calculator!")
        break

    elif choice == "10":
        print("\n========== HISTORY ==========")

        if len(history) == 0:
            print("No calculations performed yet.")
        else:
            for item in history:
                print(item)

        continue

    elif choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:

        numbers = get_numbers()

        if choice == "1":
            result = addition(numbers)
            operation = "Addition"

        elif choice == "2":
            result = subtraction(numbers)
            operation = "Subtraction"

        elif choice == "3":
            result = multiplication(numbers)
            operation = "Multiplication"

        elif choice == "4":
            result = division(numbers)
            operation = "Division"

            if result is None:
                print("\nError! Division by zero is not allowed.")
                continue

        elif choice == "5":
            result = modulus(numbers)
            operation = "Modulus"

            if result is None:
                print("\nError! Modulus by zero is not allowed.")
                continue

        elif choice == "6":
            result = power(numbers)
            operation = "Power"

        elif choice == "7":
            result = sum(numbers) / len(numbers)
            operation = "Average"

        elif choice == "8":
            result = max(numbers)
            operation = "Maximum"

        elif choice == "9":
            result = min(numbers)
            operation = "Minimum"

        print("\n-----------------------------")
        print("Numbers :", numbers)
        print("Operation:", operation)
        print("Result  :", result)
        print("-----------------------------")

        history.append(
            f"{operation} of {numbers} = {result}"
        )

    else:
        print("\nInvalid choice! Please select from 0 to 10.")