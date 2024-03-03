my_list = [1, 2, 3, 4, 2, 3, 5, 6, 7, 1]
print("Original list:", my_list)

# Create an empty list to store unique elements
unique_elements = []

# Iterate through the list
for item in my_list:
    # If the item is not already in the unique_elements list, add it
    if item not in unique_elements:
        unique_elements.append(item)

print("List with duplicates removed:", unique_elements)

# output

"""
    Original list: [1, 2, 3, 4, 2, 3, 5, 6, 7, 1]
    List with duplicates removed: [1, 2, 3, 4, 5, 6, 7]

"""