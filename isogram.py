def is_isogram(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

# Test
print(is_isogram("Hello"))  # Output: False
print(is_isogram("world"))  # Output: True
