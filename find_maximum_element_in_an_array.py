arr = [10,4,43,99,89,110]

max = arr[0]

for i in arr[1:]:
    if i > max:
        max = i

print("The maximum element in an array is:",max)

# output

"""
    The maximum element in an array is: 99

"""