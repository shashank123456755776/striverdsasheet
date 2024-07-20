# count subarray with given sum,positiveand negative numbers :
# contiguos part of the arrays:
# time complexcity will be 0(n3)

# prefix sum concepts using hash map as dictionaries:
arr = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
k = 3
count = 0

for i in range(len(arr)):
    sum = 0
    for j in range(i, len(arr)):
        sum += arr[j]
        if sum == k:
            count += 1

print(count)
      

# Optimized in o(n2) time complexcity:
k = 3
count = 0

for i in range(len(arr)):
    sum = 0
    for j in range(i, len(arr)):
        sum += arr[j]
        if sum == k:
            count += 1

print(count)

# optimal solution:
dic = {0: 1}
count = 0
sum = 0

for i in range(len(arr)):
    sum += arr[i]
    if sum - k in dic:
        count += dic[sum - k]
    if sum in dic:
        dic[sum] += 1
    else:
        dic[sum] = 1

print(count)

          
     


               

