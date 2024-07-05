def merge_sorted_list(list1, list2):
    value = sorted(list1+list2)
    return value

new = input("Enter the list value separate by commas:")    # Here input get from user for the list values
list1 = [int(x) for x in new.split(',')]                # int(x) used for convert string to numbers
list2 = [2, 4, 6, 8, 10]
both = merge_sorted_list(list1, list2)
print(f"The two lists are {list1} and {list2} then the merging list is:", both)

# output

"""
    Enter the list value separate by commas:1,3,5,7,9
    The two lists are [1, 3, 5, 7, 9] and [2, 4, 6, 8, 10] then the merging list is: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
