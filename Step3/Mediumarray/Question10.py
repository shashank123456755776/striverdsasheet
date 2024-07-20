# Set martix zero 
# need to rivision questions:
# We have n*m matrix
# Set every 1 in row and column marked as  zeros in those column and where zeros containing

# first marked all 1s as -1 along row and column for each zeros
# and set all -1 as zeros and we will get answers,but time complexcity will be o(n3)
# brute forec solution has time complexcity  will be o(n3)
# reduce it in o(n2)
# code looks like
# time complexcity will be o(n*m) and at wrost cases o(n2) and space complexcity will o(n)+o(m)
# this is bettter solution
def set_zeros(arr):
    rows = len(arr)
    cols = len(arr[0])
    zero_rows = set()
    zero_cols = set()

    # Find zero positions and mark rows and columns
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Set zeros in rows
    for row in zero_rows:
        for j in range(cols):
            arr[row][j] = 0

    # Set zeros in columns
    for col in zero_cols:
        for i in range(rows):
            arr[i][col] = 0

    return arr

# Example usage
arr = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]

result = set_zeros(arr)
print(result)
for row in result:
    print(row)

# Optimal Approachses:o(1)
# again i will do this questions:


