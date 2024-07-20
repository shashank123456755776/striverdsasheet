# Intersection of Two Arrays
# Brute force Approaches 
# Time complexcity is o(n*m) ,for same length array  is o(N**2) and space complexcity is o(N)

ar = [1, 2, 2,3, 4, 6, 7]
ar1 = [2, 3, 5, 1, 2]
ar2 = []
for i in range(len(ar)):
    if ar[i] in ar1 and ar[i] not in ar2:
          ar2.append(ar[i])
print(ar2)
 
# 0ptimal Approaches 
# On Sorted Arrays
# By Using Two Pointers 
a1=[1,2,5,6,7,8]
a2=[2,3,5,8,9]
ans=[]
j=0
i=0
while i<len(a1) and j<len(a2):
     if a1[i]<a2[j]:
          i+=1
     elif a1[i]>a2[j]:
          j+=1
     else:
          ans.append(a1[i])   
          i+=1
          j+=1
print(ans)          

     

