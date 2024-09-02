# Function: is_even
def is_even(number):
    """
    This function checks if a number is even.
    It returns True if the number is even, otherwise False.
    """
    return number % 2 == 0

# User input for is_even
print("\n--- is_even Function ---")
number = int(input("Enter a number for is_even: "))
print(f"Is {number} even?", is_even(number))
