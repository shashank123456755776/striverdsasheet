from math import isqrt

a = 36
ar = []

# Using isqrt to get the integer square root
for i in range(1, isqrt(a) + 1):
    if a % i == 0:
        ar.append(i)
        if a // i != i:
            ar.append(a // i)

print(ar)
              