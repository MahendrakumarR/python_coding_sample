# Reverse a string
def reverse():
    name = input("Enter the String:")
    print("The reversed string is :",name[::-1])
reverse()

# output

"""
    Enter the String:Hello
    olleH
"""

# or

def reve(n):
    return n[::-1]
v = input("Enter the string:")
n = reve(v)
print("Given string is:", v)
print("Reversed string is:", n)

# output

"""
    Enter the string:kerala
    Given string is: kerala   
    Reversed string is: alarek

"""

# or

s = input("Enter the string:")
v = ' '
for i in s:
    v = i + v         
    # here 'v = v + i' work like this // here ' v = i + v work like this
""" 
    m                                           m
    ma                                          am
    mah                                         ham
    mahe                                        eham
    mahen                                       neham
    mahend                                      dneham
    mahendr                                     rdneham
    mahendra                                    ardneham
    mahendran                                   nardneham      """

print("The reversed string is :",v)      

# output
"""
        Enter the string:Mahendran
        The reversed string is : nardnehaM 
"""    