def find_common_elements(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return list(set1.intersection(set2))

# Test
print(find_common_elements([2, 3, 4, 1], [1, 3, 4, 5, 6]))   # Output: [3, 4]
