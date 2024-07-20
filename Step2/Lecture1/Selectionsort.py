
# Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum (or maximum, depending on sorting order) element from the unsorted portion of the array and moving it to the beginnin

arr = [6, 4, 8, 1, 9, 2, 0]

for i in range(len(arr)-1):
    min_index = i
    for j in range(i , len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)
