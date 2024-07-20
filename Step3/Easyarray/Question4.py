# Remove duplicate in place sorted array:
# brute force using set
# time complexcity is o(N) and space complexcity is o(N)+o(1)
# set remove automatically remove the duplicate
# set in python use internally hash table data structure:
ar=[1,1,1,2,3,5,2]
p=set(ar)
print(list(p))


# by using dictonaries the time complescity will be o(N)and space complexcity is o(1)+o(N)

dic={}
for i in range(len(ar)):
    if ar[i] not in dic:
        dic[ar[i]]=1
  
print(list(dic))

# by using two pointer  approach 
# time 0(N) and space o(1),in question "In place" means without takes extra spaces
k=0
for j in range(1,len(ar)):
    if ar[j]!=ar[k]:
        ar[k+1]=ar[j]
        k+=1
del ar[k:]        
print(ar)        