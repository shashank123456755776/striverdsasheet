# 2))second larget elements in the arrays,contain dupicate also
# brute force  approach time complexcity is N+Nlog(N)
# sort function has takes  o(nlogn)  time
ar=[5,2,4,8,7,7,2]
ar.sort()
for i in range(len(ar)-2,-1,-1):
    if ar[i]!=ar[i+1]:
      print(ar[i])
      break
# better approach time complexcity is o(2N)
# but  if we using this approach no elemnts in arrays will be negative 
maxi=0
second_largest=-1
for i in range(0,len(ar)):
    if ar[i]>maxi:
        maxi=ar[i]
for i in range(0,len(ar)-1):
   if ar[i]>second_largest and second_largest<ar[-1]:
       second_largest=ar[i]  
print(second_largest)       
  
# optimal approach time compelxcity is 0(N)
secondlargest = -1
largest = ar[0]

for num in ar:
    if num > largest:
        secondlargest = largest
        largest = num
    elif num > secondlargest and num != largest:
        secondlargest = num

print(secondlargest)