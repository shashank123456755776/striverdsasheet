# # Three apporoaches Brute forces 
# Solution 1: Brute force

# Intuition: Simply traverse from 1 to min(a,b) and check for every number.

# Approach: 

# Traverse from 1 to min(a,b).
# And check if i is divisible by both a and b.If yes store it in the answer.
# Find the maximum value of i which divides both a and b.
# Code
# Time o(n) ans space 0(1)
def fun(n1, n2):
    #  list comprhension
    p=0
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            p=i
    return p
     

n1 = int(input("Enter a number one: "))  
n2 = int(input("Enter a number two: "))  
p = fun(n1, n2)  
print(p)

# second method loops goings for square roots times



