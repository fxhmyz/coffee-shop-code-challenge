# Function: reverse_string
def reverse_string(text):
    """
    This function takes a string as input and returns the string reversed.
    """
    return text[::-1]

# User input for reverse_string
print("\n--- reverse_string Function ---")
text = input("Enter a string for reverse_string: ")
print("Reversed string:", reverse_string(text))
