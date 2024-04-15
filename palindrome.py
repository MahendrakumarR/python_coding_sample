
# palindrome


def pal():
    if name == name[::-1]:
        print(f'The given string {name} is palindrome')
    else:
        print(f'The given string {name} is not a palindrome')
name = input("Enter the string:")
pal()

# output

"""
    Enter the string:madam
    The given string madam is palindrome

"""

# or

pali = input("Enter the String:")

if pali == pali[::-1]:
    print(f'The given string {pali} is palindraome')
else:
     print(f'The given string {pali} is not a palindraome')

# output

"""
    Enter the String:hello
    The given string hello is not a palindraome
"""

# or

s = input("Enter the string:")
v = ''
for i in s:
    v = i + v  
print(v)

if s == v:
    print(f"The given string {s} is palindrome")
else:
    print(f"The given string {s} is not a palindrome")