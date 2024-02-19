# fibonacci sequence

def fibonacci(n):
    list = [0,1]
    while len(list)<n:
        next_number = list[-1] + list[-2]   
        list.append(next_number)
    return list[:n]

number = 10
store = fibonacci(number)
print(f"The fibonacci series of {number} is {store}")

# output 
"""
   The fibonacci series of 10 is [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] 

"""
# or

def fibonacci(n):
    list = [0,1]
    while len(list)<n:
        next_number = list[0] + list[-2]   # only change the index value
        list.append(next_number)
    return list[:n]

number = 10
store = fibonacci(number)
print(f"The fibonacci series of {number} is {store}")

# output 
"""
   The fibonacci series of 10 is [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

"""