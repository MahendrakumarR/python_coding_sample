# Star print 
# up to down

for i in range(1,7):  # range 1 to 6
    print("*" * i)    # "*" * 1 = * , "*" * 2 = ** ,....
print("")            # finaly give space after execute the code

# output 
"""
    *
    **
    ***
    ****
    *****
    ******
"""
# Star print 
# down to up

for i in range(6,0,-1):  # range 6 to 1 then -1 is decrease one by one 6 to 0
    print("*" * i)    # "*" * 1 = * , "*" * 2 = ** ,....
print(" ")

# output 
"""
    ******
    *****
    ****
    ***
    **
    *
"""

n=5
for i in range(1,n+1): # here why use {n+1} n = 5 limits already declare. but here not give(1,n) -this is wrong becuase range take ( 1 to 4) so use (n+1) 
    print(" " * (n-i) + "*" * (2 * i - 1) + " " * (n-i) )
print(" ")

# output

"""
    *    
   ***
  *****
 ******* 
*********

"""

# pyramid

for i in range(1,6):
    print(" " * (5-i) + "*" * i  + " " * (5-i) ) # here ( " " * (5 - i)) -is used for space beginig of the star then, ( "*" * (2 * i - 1)) -is used to howmany stars are print, star print after give space using ( " " * (5 - i))  
print()
# output

"""
    *
   **
  ***
 **** 
*****

"""

for i in range(6,1,-1): # -1 for decreasing the value
    print(" " * (6-i) + "*" * (2 * i - 1) + " " * (6-i) ) # here ( " " * (6 - i)) -is used for space beginig of the star then, ( "*" * (2 * i - 1)) -is used to howmany stars are print, star print after give space using ( " " * (6 - i))  
print(" ")
# output

"""

***********
 *********
  *******
   *****   
    ***

"""



