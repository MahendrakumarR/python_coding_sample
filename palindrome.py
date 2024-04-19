
# palindrome


def pal():
    if name == name[::-1]:
        print(f'The given string {name} is Palindrome')
    else:
        print(f'The given string {name} is not a Palindrome')
name = input("Enter the string:")
pal()

# output

"""
    Enter the string:madam
    The given string madam is Palindrome

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

s = input("Enter the String:")
v = ''
for i in s:
    v = i + v  
print(v)

if s == v:
    print(f"The given string {s} is palindrome")
else:
    print(f"The given string {s} is not a palindrome")