# Arithmetic calculator
# This program implements a basic arithmetic calculator that allows the user to perform one of four mathematical operations: Add, Subtract, Multiply and Divide.

# Step 1. Request the numbers.
    # - input() -> receives the data entered by the user.
    # - float() -> converts the input data to a floating-point number.

# Step 2. Request the operation.
    # - The method: .upper() -> converts any letter to uppercase. This avoids problems if the user types in lowercase.

# Step 3. Evaluate the operation
    # - The program uses a structure: "if", "elif", "else" to evaluate the operation entered by the user.

# Step 4. Validate an incorrect operation.
    # - If the user enters any other letter, the program displays: "Invalid operation. Please enter A, S, M, or D."

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter the operation (A - Add, S - Subtract, M - Multiply, D - Divide): ").upper()

if operation == "A":
    addition = num1 + num2
    print(f"\nThe sum is: {addition}")

elif operation == "S":
    subtraction = num1 - num2
    print(f"\nThe subtraction is: {subtraction}")

elif operation == "M":
    multiplication = num1 * num2
    print(f"\nThe multiplication is: {multiplication}")

elif operation == "D":
    if num2 != 0:
        division = num1 / num2
        print(f"\nThe division is: {division:.2f}")
    else:
        print("\nError: Cannot divide by zero.")

else:
    print("\nInvalid operation. Please enter A, S, M, or D.")
