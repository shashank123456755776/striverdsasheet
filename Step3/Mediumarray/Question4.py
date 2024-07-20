
# Maximum Subarray Sum
# brute force
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
le = 0  

for i in range(len(arr)):
    for j in range(i, len(arr)):
        subarray_sum =0  # Reset the sum for each new subarray
        for k in range(i, j+1):
            subarray_sum += arr[k]
        le = max(le, subarray_sum)  # Update the maximum subarray sum

print(le)
# but above code time will be o(n3) 
# lets 0ptimized it in o(n2)

for i in range(len(arr)):
    sum=0
    for j in range(len(arr)):
        sum=sum+arr[j]
    le=max(le,sum)    
print(le)    

# Optimal Solution 
# Kadens Algorithm
# So this algorithm helps us to solve such problems:
# time complexcity is 0(N) and o(1) space complexcity

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
maxi = arr[0]  # Initialize the maximum subarray sum with the first element of the array
sum = 0
start = 0  # Initialize the starting index of the current subarray
anstart = -1
ansend = -1

for i in range(len(arr)):
    sum += arr[i]
    
    # Check if the current sum is greater than the maximum sum so far
    if sum > maxi:
        maxi = sum
        anstart = start  # Update the start index of the maximum sum subarray
        ansend = i  # Update the end index of the maximum sum subarray
    
    # If sum becomes negative, reset sum and move the start index to the next element
    if sum < 0:
        sum = 0
        start = i + 1

print("Maximum Subarray Sum:", maxi)
print("Start Index:", anstart)
print("End Index:", ansend)






