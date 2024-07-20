# Rotate matrix by 90 degress:
# brute force
# time and space complexcity will be o(n2)
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def rotate(arr):
    rows = len(arr)
    columns = len(arr[0])
    ans = [[0] * rows for _ in range(columns)]  # Initialize ans with the correct size
    
    for i in range(rows):
        for j in range(columns):
            ans[j][rows - 1 - i] = arr[i][j]
    
    return ans

rotated_matrix = rotate(arr)
print(rotated_matrix)

# optimal solution first tranpose the matrix and reverse every row:
# In this question we have one hack that ,align with diagonal swap right half of the diagonal to the left half elements:


def rotate(matrix):
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]

# Test the function
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(arr)
print(arr)

