# traverses matrix in Spiral Manner:
# Optimal Solutions:
# Optimal Solutions:
# Optimal Solutions:
# Optimal Solutions:
# Optimal Solutions:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row = len(matrix)
col = len(matrix[0])
left = 0
right = col - 1
top = 0
bottom = row - 1
ans = []


def spiral(matrix):
    global left, right, top, bottom
  
    while left <= right and top <= bottom:
        # Traverse top row from left to right
        for i in range(left, right + 1):
            ans.append(matrix[top][i])
          
        top += 1

        # Traverse right column from top to bottom
        for i in range(top, bottom + 1):
            ans.append(matrix[i][right])
   
        right -= 1

        # Check if there are remaining rows to traverse
        if top <= bottom:
            # Traverse bottom row from right to left
            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
             
            bottom -= 1

        # Check if there are remaining columns to traverse
        if left <= right:
            # Traverse left column from bottom to top
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
               
            left += 1

    return ans


p = spiral(matrix)
print(p)




