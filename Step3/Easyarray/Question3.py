# check array is sorted or not sorted
# time complexcity is o(N) best time it is :
ar=[1,2,3,6,4,5]
flag=False
for i in range(1,len(ar)):
    if ar[i]>ar[i-1]:
        flag=True
    else:
        flag=False
if not flag:
    print(True)
else:
    print(False )           
        
