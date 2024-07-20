ar = [64, 56, 84, 100, 74, 1, 3]

def sorts(ar):
    j = 0
    while j < len(ar) - 1:
        if ar[j] > ar[j + 1]:
            ar[j], ar[j + 1] = ar[j + 1], ar[j]
        j += 1

def bubble_sort(ar, n):
    if n == 1:
        return
    
    sorts(ar)  # Using sorts function to perform one pass of bubble sort
    
    bubble_sort(ar, n - 1)  # Recursive call for the remaining elements

# Call the function to sort the array
bubble_sort(ar, len(ar))

print(ar)
