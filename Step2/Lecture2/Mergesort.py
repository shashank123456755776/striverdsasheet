# divide and merge algorithm 
# recursion we use to solve such problems:
# here we use functional recursion ,means when we see that we need a function return then we used it
# time complexcity of merge sort is o(nlogn) and its space complexicty is o(n)
def mergesort(ar, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    mergesort(ar, low, mid)
    mergesort(ar, mid + 1, high)
    merge(ar, low, mid, high)

def merge(ar, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    
    while left <= mid and right <= high:
        if ar[left] <= ar[right]:
            temp.append(ar[left])
            left += 1
        else:
            temp.append(ar[right])
            right += 1
    
    while left <= mid:
        temp.append(ar[left])
        left += 1
    
    while right <= high:
        temp.append(ar[right])
        right += 1
    
    for i in range(low, high + 1):
        ar[i] = temp[i - low]

# Example usage:
ar = [3, 1, 2, 4, 1, 5, 2, 6, 4]
mergesort(ar, 0, len(ar) - 1)
print(ar)
