# Function: calculate_factorial
def calculate_factorial(n):
    """
    This function calculates the factorial of a non-negative integer n.
    The factorial is the product of all positive integers less than or equal to n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# User input for calculate_factorial
print("\n--- calculate_factorial Function ---")
n = int(input("Enter a non-negative integer for calculate_factorial: "))
print("Factorial:", calculate_factorial(n))
