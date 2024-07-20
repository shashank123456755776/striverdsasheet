# Maximum Consecutive Ones:
# optimal
ar=[1,1,2,3,1,1,1,5,1,1,6]
# time complexcity is o(N)
ar = [1, 1, 2, 3, 1, 1, 1, 5, 1, 1, 6]
maxi = 0  # Variable to store the maximum consecutive ones found
count = 0  # Variable to keep track of the current consecutive ones count

# Iterating through the array
for i in range(len(ar)):
    # If the current element is 1, increment the count of consecutive ones
    if ar[i] == 1:
        count += 1
    else:
        # If the current element is not 1, reset the count of consecutive ones
        count = 0
    # Update maxi to keep track of the maximum consecutive ones found so far
    maxi = max(maxi, count)

# Print the maximum consecutive ones found
print(maxi)

    


