# Longest Subarrays with Sum K:(positive)
# Subarrays---Contigous part of the array
# brute forces:
ar = [1, 2, -1, 0, 1, 1, 1, 4, 2, 3]
k = 3

max_len = 0

for i in range(len(ar)):
    for j in range(i, len(ar)):
        current_sum = 0
        for num in ar[i:j+1]:
            current_sum += num
        if current_sum == k:
            max_len = max(max_len, j - i + 1)

print(max_len)

# let optimize this brute in o(n2)


max_len = 0

for i in range(len(ar)):
    current_sum = 0
    for j in range(i, len(ar)):
        current_sum += ar[j]
        if current_sum == k:
            max_len = max(max_len, j - i + 1)

print(max_len)



# optimized using hashing with this code with run for all postive ,negative and zeros:
# space will be 0(N) and time will be 0(N)
dic = {}
max_len = 0
current_sum = 0
for i in range(len(ar)):
    current_sum += ar[i]
    
    if current_sum == k:
        max_len = max(max_len, i + 1)
        
    elif current_sum - k in dic:
        max_len = max(max_len, i - dic[current_sum - k])
        
    if current_sum not in dic:
        dic[current_sum] = i

print(max_len)

# 0ptimal Solution for postive value in arrays only buy using two pointers two pointers:
# o(n2)
arr = [1, 2, 3, 1, 1, 1, 1, 3, 3]
i = 0
j = 0
le = 0
sum = 0
k = 4
while j < len(arr):
    sum += arr[j]
    if sum < k:
        j += 1
    elif sum == k:
        le = max(le, j - i + 1)
        j += 1  # Move the right pointer to continue the exploration
    else:
        if i < len(arr):  # Check if left pointer i is within bounds
            sum -= arr[i]  # Adjust the left pointer to reduce the sum
            i += 1
      
print(le)
