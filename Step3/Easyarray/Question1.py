# 1)) Largest elements in the arrays:
# brute force methods :
# time complxcity is o(nlogn) and space compexcity is o(1)
ar=[5,2,4,8,7,7,2]
ar.sort()
print(ar[-1])
 

# optimal solution
# time complexsity is o(n) and  space compexcity is o(1)
maxi=0
for i in range(0,len(ar)):
    if ar[i]>maxi:
        maxi=ar[i]
print(maxi)        

