# Function: sort_by_age
def sort_by_age(persons):
    """
    This function takes a list of tuples where each tuple contains a name and an age.
    It returns the list sorted by age in ascending order.
    """
    return sorted(persons, key=lambda x: x[1])

# User input for sort_by_age
print("\n--- sort_by_age Function ---")
num_people = int(input("Enter the number of people for sort_by_age: "))
people = []
for _ in range(num_people):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    people.append((name, age))

print("Sorted by age:", sort_by_age(people))
