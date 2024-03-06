def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is found at mid
        if arr[mid] == target:
            return mid
        
        # If target is smaller, ignore right half
        elif arr[mid] > target:
            right = mid - 1
        
        # If target is larger, ignore left half
        else:
            left = mid + 1
    
    # If target is not present in the array
    return -1

# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 9
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} is present at index {result}.")
else:
    print("Element not found.")
