def are_anagrams(str1, str2):
    # Remove spaces and convert strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the lengths of the strings are equal
    if len(str1) != len(str2):
        return False
    
    # Sort the characters in both strings and compare
    return sorted(str1) == sorted(str2)

# Example usage:
string1 = "listen"
string2 = "silent"
if are_anagrams(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")

# output
"""
    listen and silent are anagrams.

"""

s1 = input("Enter the first word:")
s2 = input("Enter the second word:")

s1 = s1.replace(" ","".lower())
s2 = s2.replace(" ","".lower())

if sorted(s1) == sorted(s2):
    print(f'The given string {s1} and {s2} are anagram')
else:
    print(f'The given string {s1} and {s2} are not anagram')

