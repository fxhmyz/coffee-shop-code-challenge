# Function: count_vowels
def count_vowels(text):
    """
    This function counts the number of vowels (a, e, i, o, u)
    in a given string, ignoring case sensitivity.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

# User input for count_vowels
print("\n--- count_vowels Function ---")
text = input("Enter a string for count_vowels: ")
print("Number of vowels:", count_vowels(text))
