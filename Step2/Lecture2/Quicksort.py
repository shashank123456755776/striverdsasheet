# the quick sort has time complexcity as o(nlogn) and space complexcity is 0(1)
#  Quick sort is a popular sorting algorithm used to sort a list or an array of elements. It follows the divide-and-conquer approach, where it recursively divides the list into smaller sublists based on a chosen pivot element, and then sorts those sublists.
#picked a pivot and place it in correct place return sorted arrays 
# smaller on the left and larger wil be the right 

def sortii(ar, low, high):
    pivot = ar[low]
    i = low
    j = high
    while i < j:
        while i <= high and ar[i] <= pivot:
            i += 1
        while ar[j] > pivot and j >= low:
            j -= 1
        if i < j:
            ar[i], ar[j] = ar[j], ar[i]
    ar[low], ar[j] = ar[j], ar[low]
    return j

def quicksort(ar, low, high):
    if low < high:
        partition_index = sortii(ar, low, high)
        quicksort(ar, low, partition_index - 1)
        quicksort(ar, partition_index + 1, high)

ar = [4, 6, 2, 5, 7, 9, 1, 3]
quicksort(ar, 0, len(ar) - 1)
print(ar)
