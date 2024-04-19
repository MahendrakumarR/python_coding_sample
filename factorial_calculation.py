# factorial 

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result*=i
    return result
n = int(input("Enter the Number:"))
val = factorial(n)
print(f"The factorial of {n} is :{val}")

# output

"""
    Enter the Number:5
    The factorial of 5 is :120

"""

# or

s = int(input("Enter the Number:"))
final = 1

for i in range(1,s+1):
    final = final * i
print(f"The factorial of {s} is :",final)

# output
"""
    Enter the Number:10
    The Factorial of 10 is : 3628800

"""

