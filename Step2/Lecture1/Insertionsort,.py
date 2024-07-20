# Takes an elements and placed it in correct orders:
ar = [9, 14, 15, 12, 6, 3, 13]

for i in range(1, len(ar)):
    for j in range(i, 0, -1):  # Corrected the range
        if ar[j] < ar[j - 1]:
            ar[j], ar[j - 1] = ar[j - 1], ar[j]

print(ar)
