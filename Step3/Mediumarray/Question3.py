# Majority elements greater than n/2 times:
# Brute force methods:
ar = [2, 2, 3, 3, 1, 2, 2]
for i in range(len(ar)):
    count = 0
    for j in range(len(ar)):
        if ar[j] == ar[i]:
            count += 1
    if count > len(ar) // 2:
        print(count)
        break
# Optimal Approaches
# Hasing we generally used when we need to track somethings:
# Time complexcity is o(2N)==o(N) and space complexcity is o(1)
dic={}
for i in ar:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for key,value in dic.items():
     if value>len(ar)//2:   
         print(value)     
         break    

# Mores Voting Algorithm:,this is also optimal apparaoches:
arr = [7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 5, 5, 5, 5]
el = 0
count = 0
final = 0

for i in range(len(arr)):
    if count == 0:
        el = arr[i]
        count += 1
    elif el == arr[i]:
        count += 1
    else:
        count -= 1

for j in range(len(arr)):
    if arr[j] == el:
        final += 1

print(final)

