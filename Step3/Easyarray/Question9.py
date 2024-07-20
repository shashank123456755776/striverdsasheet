# Union of two sorted arrays:
# add both array but no elements will be repeat in resulting ararys:
# | if using this integers tehn it is called as bitwise or operators
# between set if we are using then it removing common elemnst
# brute forec
ar = [1, 1, 3, 4, 5, 6]
ar1 = [3, 4, 4, 5, 6]

p = set(ar) | set(ar1)
result = list(p)
print(result)
# brute force o(n+m)+o(n)=o(n)
ar=[1,1,3,4,5,6]
ar1=[3,1,4,5,6]
p=set(ar)
for i in ar1:
    p.add(i)      
print(list(p))    

# optimal approaches using two pointers:
# o(n+m) is time and space commplexcity
ar = [1, 1, 3, 4, 5, 6]
ar1 = [3, 1, 4, 5, 6]

ar2 = []
k = 0
m = 0

while k < len(ar) and m < len(ar1):
    if ar[k] < ar1[m]:
        if ar[k] not in ar2:
            ar2.append(ar[k])
        k += 1
    elif ar[k] > ar1[m]:
        if ar1[m] not in ar2:
            ar2.append(ar1[m])
        m += 1
    else:  # ar[k] == ar1[m]
        if ar[k] not in ar2:
            ar2.append(ar[k])
        k += 1
        m += 1

# Add remaining elements from ar, if any
while k < len(ar):
    if ar[k] not in ar2:
        ar2.append(ar[k])
    k += 1

# Add remaining elements from ar1, if any
while m < len(ar1):
    if ar1[m] not in ar2:
        ar2.append(ar1[m])
    m += 1

print(ar2)





