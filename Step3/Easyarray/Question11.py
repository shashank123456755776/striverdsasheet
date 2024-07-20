# find the missing elemnsts in arrays:
# brute force time oxmplcity is o(n*m) and space is 0(1)
n=5
ar=[1,2,4,5]
for i in range(1,n):
    if i not in ar:
        print(i)
        break

# optimal  approaches: 
# here time complexcity is    o(n) ans space complexcity is 0(1)
for i in range(0,len(ar)):
    if ar[i+1]-ar[i]==2:
        print(ar[i]+1)
        break
# also can be donw using hash means dictinaries
# also can be done using sum which is optimal
sum=n*(n+1)/2
sum1=0
for i in range(len(ar)):
    sum1=sum1+ar[i]
p=int(sum-sum1)
print(p)    

# by using xor
# Example 2^2 =0,2^2^2=0... using this for finding missing values

# Example 2^2 =0,2^2^2=0... using this for finding missing values
# Example 2^2 = 0, 2^2^2 = 0... using this for finding missing values
# time complexcity is o(2n) this is better approaches
xor1 = 0
for i in range(1, n + 1):  # XOR of consecutive numbers from 1 to n
    xor1 = xor1 ^ i  

xor2 = 0
for num in ar:  # XOR of all elements in the array
    xor2 = xor2 ^ num  

print(xor1 ^ xor2)  # XOR of the two results to find the missing value


# So also do in one loop

# Example 2^2 = 0, 2^2^2 = 0... using this for finding missing values

n = len(ar) + 1  # Assuming there's one missing element in the range

xor_result = 0
for i in range(1, n + 1):  # XOR of consecutive numbers from 1 to n
    if i <= len(ar):
        xor_result = xor_result ^ i ^ ar[i - 1]  # XOR of consecutive number and array element
    else:
        xor_result = xor_result ^ i  # If i exceeds the length of ar, XOR it alone

print(xor_result)  # Resulting XOR will be the missing value






