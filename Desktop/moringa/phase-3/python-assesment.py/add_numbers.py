# Function: add_numbers
def add_numbers(num1, num2):
    """
    This function takes two parameters, num1 and num2,
    and returns their sum.
    """
    return num1 + num2

# User input for add_numbers
print("\n--- add_numbers Function ---")
num1 = float(input("Enter the first number for add_numbers: "))
num2 = float(input("Enter the second number for add_numbers: "))
print("Result of add_numbers:", add_numbers(num1, num2))
