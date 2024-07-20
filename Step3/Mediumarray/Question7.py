# Next Permutation 
# very important questions
# Permutation means  all the Ways in Sorted order when we will rearrange the numbers:
ar1=[]
# Brute force,it take smore times n!*n
# three steps require for this 
# 1st generates all possible permutation:  we using Recursions
# 2nd  liner search
# 3rd Next Permutation
ar = [1, 2, 3]
ar1 = []

def per(ar, i, j):
    if i == len(ar):
        return
    while j < len(ar) - 1:
        ar[j], ar[j + 1] = ar[j + 1], ar[j]  # Swap elements
        ar1.append(ar[:])  # Append a copy of the list
        return per(ar, i, j + 1)  # Recursively call with incremented j
    return per(ar, i + 1, 0)  # Recursively call with incremented i and reset j to 0

per(ar, 0, 0)
print(ar1)
for i in range(len(ar1)):
    if ar1[i]==ar and i<len(ar1)-2:
        print(i+1)
    elif ar1[i]==ar1[-1]:
        print(ar[0])  

# Prefix diffrence that gives all possible sets means 
# As examples raj,rax,rbx
# so to solve such problems we have following observation as discussed below:
# 1 longer prefix match a[i]<a[i+1],dipp,find the break point
# 2 find >1,but the smallest one so that you stay close
# 3 try to place in sorted order after placed 3 in 1 place
# If their is No diip then reverse the given an array will be answer if index =-1,means it will base case

arr = [2, 1, 5, 4, 3, 0, 0]
index = -1

# Find the index of the longest prefix where a[i] < a[i+1]
for i in range(len(arr)-2, -1, -1):
    if arr[i] < arr[i+1]:
        index = i
        break

# If no such prefix exists, reverse the array
if index == -1:
    arr = arr[::-1]
else:
    # Find the smallest element > arr[index]
    for i in range(len(arr)-1, index, -1):
        if arr[i] > arr[index]:
            # Swap arr[i] and arr[index]
            arr[i], arr[index] = arr[index], arr[i]
            break

    # Reverse the elements after index
    arr[index+1:] = arr[index+1:][::-1]

print(arr)

# so after optimzing time complexcity is o(3N) and space conplexcity is o(1)


