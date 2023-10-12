import math

def addition():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

def subtraction():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# Define functions for other operations (multiplication, division, etc.)

def calculate_pi_with_input():
    try:
        user_value = float(input("Enter a number to calculate π (pi): "))
        pi_value = user_value * math.pi
        print(f"{user_value} times π (pi) is approximately {pi_value:.6f}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def calculate_logarithm():
    try:
        base = float(input("Enter the base for the logarithm: "))
        number = float(input("Enter the number for the logarithm: "))
        result = math.log(number) / math.log(base)
        print(f"Logarithm base {base} of {number} is approximately {result:.6f}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

def calculate_power():
    try:
        base = float(input("Enter the base: "))
        exponent = float(input("Enter the exponent: "))
        result = math.pow(base, exponent)
        print(f"{base} to the power of {exponent} is {result}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

def calculate_root():
    try:
        degree = float(input("Enter the degree of the root: "))
        radicand = float(input("Enter the radicand: "))
        result = math.pow(radicand, 1 / degree)
        print(f"{degree}-th root of {radicand} is approximately {result:.6f}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

def calculate_factorial():
    try:
        number = int(input("Enter a number to calculate factorial: "))
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            factorial = 1
            for i in range(1, number + 1):
                factorial *= i
            print(f"Factorial of {number} is {factorial}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def calculate_sine():
    try:
        angle_degrees = float(input("Enter an angle in degrees: "))
        angle_radians = math.radians(angle_degrees)
        result = math.sin(angle_radians)
        print(f"Sine of {angle_degrees} degrees is approximately {result:.6f}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def calculate_cosine():
    try:
        angle_degrees = float(input("Enter an angle in degrees: "))
        angle_radians = math.radians(angle_degrees)
        result = math.cos(angle_radians)
        print(f"Cosine of {angle_degrees} degrees is approximately {result:.6f}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def calculate_tangent():
    try:
        angle_degrees = float(input("Enter an angle in degrees: "))
        angle_radians = math.radians(angle_degrees)
        result = math.tan(angle_radians)
        print(f"Tangent of {angle_degrees} degrees is approximately {result:.6f}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    print("***** Calculator *****")
    print("----------- Instructions -----------")
    print("+ for addition\n- for subtraction\n* for multiplication\n/ for division")
    print("** for power\nr for root\n! for factorial\nsin for sine\ncos for cosine\ntan for tangent\nlog for logarithmic\npi for π (pi) with user input value")

    while True:
        operation = input("Enter the operation you want to perform: ").lower()

        if operation == "+":
            addition()
        elif operation == "-":
            subtraction()
        # Define other operation cases (multiplication, division, etc.)
        elif operation == "pi":
            calculate_pi_with_input()
        elif operation == "log":
            calculate_logarithm()
        elif operation == "**":
            calculate_power()
        elif operation == "r":
            calculate_root()
        elif operation == "!":
            calculate_factorial()
        elif operation == "sin":
            calculate_sine()
        elif operation == "cos":
            calculate_cosine()
        elif operation == "tan":
            calculate_tangent()
        else:
            print("Enter a valid operator :)")

        again = input("Do you want to calculate again? (Y/N): ").lower()
        if again != "y":
            break

if __name__ == "__main__":
    main()
