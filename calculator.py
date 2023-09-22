# Define the calculator function
def calculator():
    print("Simple Calculator")
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    while True:
        # Take user input
        user_input = input(": ")

        # Check if the user wants to quit
        if user_input == "quit":
            break
        elif user_input not in ["add", "subtract", "multiply", "divide"]:
            print("Invalid input. Please enter a valid operation.")
            continue

        # Get numbers from the user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform the selected operation
        if user_input == "add":
            result = num1 + num2
        elif user_input == "subtract":
            result = num1 - num2
        elif user_input == "multiply":
            result = num1 * num2
        elif user_input == "divide":
            if num2 == 0:
                print("Division by zero is not allowed.")
                continue
            result = num1 / num2

        # Display the result
        print("Result: " + str(result))

# Run the calculator
calculator()
