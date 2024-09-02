# Function: merge_dicts
def merge_dicts(dict1, dict2):
    """
    This function takes two dictionaries as input and merges them into one.
    If there are common keys, their values are summed up.
    """
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

# User input for merge_dicts
print("\n--- merge_dicts Function ---")
dict1 = {}
dict2 = {}

num_items1 = int(input("Enter the number of items in the first dictionary: "))
for _ in range(num_items1):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dict1[key] = value

num_items2 = int(input("Enter the number of items in the second dictionary: "))
for _ in range(num_items2):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dict2[key] = value

print("Merged dictionary:", merge_dicts(dict1, dict2))
