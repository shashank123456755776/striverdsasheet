# Sort an array with 0's,1's and 2's
# Brute Force
# Time complexcity is o(nlogn) and Space complexcity is o(1)
ar=[0,1,2,0,1,2,1,2,0,0,0,1]
ar.sort()
print(ar)
# better Approaches:
# time complexcity is o(4N) ans space complexcity is o(1)
count1=0
count2=0
count3=0
for i in range(len(ar)):
    if ar[i]==0:
        count1+=1
    elif  ar[i]==1:
        count2+=1 
    elif ar[i]==2:
        count3+=1       
for k in range(count1):
    ar[i]=k   
for l in range(count2):
    ar[i]=l
for M in range(count3):
    ar[i]=M     
print(ar)           

# Optimal  Solution using Algorithm "Dutch Natinal Flag Algorithm"
# explanation
# tree pointers we have low,mid,high
# a[mid]==0,a[mid]==1,a[mid]==2
# if a[mid]==0, swap(a[low],a[mid]),low+=1,mid+=1
# if a[mid]==1 mid+=1
# a[mid]==2 swap(a[mid],a[high]),high-=1

# Diagram help it to visualized how logics goings on ....
# 0....low-1   low 1 1 1...mid-1 unsorted high high 2 2 2 ....n-1

arr=[0,1,1,0,1,2,1,2,0,0,0]
low=0
mid=0
high=len(arr)-1
while mid<=high:
    if arr[mid]==2:
        arr[mid],arr[high]=arr[high],arr[mid]
        high-=1
    elif arr[mid]==1:
        mid+=1
    elif arr[mid]==0:
         arr[low],arr[mid]=arr[mid],arr[low]
         low+=1
         mid+=1
print(arr)         

# this appraoches is very importants 





