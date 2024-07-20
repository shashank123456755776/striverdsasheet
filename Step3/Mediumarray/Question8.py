# leaders in array
# everythingt on the right should be smaller
ar=[10,22,12,3,0,6]
# so answer shold be [22,12,6]
# brute force
# time complexcity will ne o(N2) ans space complexcity will be o(N)
# I did not extra space to solve the problems buy yes i  used extra  space to store the answers
ar = [10, 22, 12, 3, 0, 6]
ar1 = []

for i in range(len(ar)):
    is_leader = True
    for j in range(i + 1, len(ar)):
        if ar[j] > ar[i]:
            is_leader = False
            break
    if is_leader:
        ar1.append(ar[i])

print(ar1)
      
#optimal solution
# time complexcity will be o(N) AND space complexcity to store the answer will be o(N)
maxi=ar[-1]
aro=[]
aro.append(ar[-1])
for i in range(len(ar)-2,-1,-1):
    if ar[i]>maxi:
        aro.append(ar[i])
        maxi=ar[i]
print(aro[::-1])
