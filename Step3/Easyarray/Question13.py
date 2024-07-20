# find the numbers that apperas onces 
# brute foces
# time o(n2) ans space is o(1)
ar = [2, 1, 3, 5, 2, 6, 3, 6, 5]
for i in range(len(ar)):
    num = ar[i]
    count = 0
    for j in range(len(ar)):
        if num == ar[j]:
            count += 1
    if count == 1:
        print(num)
#  optimal appraches    hashing datastructure
# time complexcity is o(2N) and space complexcity is o(1)
dic={}
for i in range(len(ar)):
    if ar[i] not in dic:
         dic[ar[i]]=1
    else:
        dic[ar[i]]+=1
for key ,value in dic.items():
    if value==1:
        print(key)   
     

      

