from logo import logo


def clear():
    print('\n' * 100)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        print("Division by zero error")
        calculator()
    return n1 / n2


def is_input_valid(arg):
    numeric_check = arg.isnumeric()
    if not numeric_check:
        print("Invalid input! Try again:")
        number = float(input("input a number?: "))
        return number
    else:
        number = float(arg)
        return number


def operations_validation(math_funk):
    if math_funk in operations:
        return math_funk
    else:
        math_funk = input("Invalid operation! Please try and pick again: ")
        return math_funk


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = input("What's the first number?: ")
    num1 = is_input_valid(num1)
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_choice = input("Pick an operation: ")
        operation_symbol = operations_validation(operation_choice)
        num2 = input("What's the next number?: ")
        num2 = is_input_valid(num2)
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()


calculator()
