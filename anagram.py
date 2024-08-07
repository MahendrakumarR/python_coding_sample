def are_anagrams(str1, str2):
    # Remove spaces and convert Strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the lengths of the Strings are equal
    if len(str1) != len(str2):
        return False
    
    # Sort the characters in both Strings and compare
    return sorted(str1) == sorted(str2)

# Example usage:
string1 = "listen"
string2 = "silent"
if are_anagrams(string1, string2):
    print(f"{string1} And {string2} are Anagrams.")
else:
    print(f"{string1} And {string2} are not Anagrams.")

# Output
"""
    listen And silent are anagrams.

"""

# or

s1 = input("Enter the First Word:")
s2 = input("Enter the Second Word:")

s1 = s1.replace(" " , "".lower())
s2 = s2.replace(" " , "".lower())

if sorted(s1) == sorted(s2):
    print(f'The given string {s1} and {s2} are Anagram')
else:
    print(f'The given string {s1} and {s2} are not Anagram')

# output
"""
    Enter the First Word:listen
    Enter the Second Word:silent
    The given string listen and silent are Anagram

"""

