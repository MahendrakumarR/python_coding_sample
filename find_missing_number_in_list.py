def find_missing_number(nums):
    n = len(nums) + 1
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    missing_number = total_sum - actual_sum
    return missing_number

# Example usage:
numbers = [1, 2, 3, 4, 5, 7, 8]
missing_num = find_missing_number(numbers)
print("The Missing Number is:", missing_num)


# Output
"""
    The Missing Number is:6
"""