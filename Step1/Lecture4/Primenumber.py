from math import isqrt

a = 3
count=0

# Using isqrt to get the integer square root
for i in range(1, isqrt(a) + 1):
    if a % i == 0:
        count+=1
        if a // i != i:
            count+=1
if count==2:
    print("number is prime")     
else:
    print("numbers is not prime:")           

