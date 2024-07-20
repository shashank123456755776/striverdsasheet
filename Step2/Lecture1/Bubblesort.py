# bubble sort
# in bubble sort we just try to push maximum elemnts to the last and it will automatically givesc sorted arrys :
# push maxmimum elements to the last by adjacent swap:
ar = [7, 1, 2, 9, 0, 10, 4]
n = len(ar)
for i in range(n):
    for j in range(0, n-i-1):
        if ar[j] > ar[j+1]:
            ar[j], ar[j+1] = ar[j+1], ar[j]

print(ar)
