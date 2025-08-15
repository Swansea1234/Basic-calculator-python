# A simple calculator program that takes two numbers and an operation from the user,
# then prints the result in a specific format.

def calculate():
    """
    Asks the user for two numbers and an operation, then performs the calculation
    and prints the result.
    """
    # Use a try-except block to handle potential errors, such as invalid number input.
    try:
        # Get the first number from the user and convert it to a floating-point number.
        num1 = float(input("Enter the first number: "))
        
        # Get the mathematical operation from the user.
        operation = input("Enter a mathematical operation (+, -, *, /): ")
        
        # Get the second number from the user.
        num2 = float(input("Enter the second number: "))

        # Initialize the result variable.
        result = 0

        # Perform the calculation based on the user's input.
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            # Check for division by zero before performing the operation.
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                return # Exit the function if division by zero is attempted.
            result = num1 / num2
        else:
            # Inform the user if the operation is not recognized.
            print("Error: Invalid operation. Please use +, -, *, or /.")
            return # Exit the function if the operation is invalid.

        # Print the result in the requested format.
        print(f"{num1} {operation} {num2} = {result}")

    except ValueError:
        # This block runs if the user enters something that isn't a valid number.
        print("Error: Invalid input. Please enter numbers only.")

# Call the function to run the program.
if __name__ == "__main__":
    calculate()
