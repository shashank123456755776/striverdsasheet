# Left rotate arrays by one places:
# Optimal approaches
# time complexcity is o(N) and space compexcity is o(1)
# but if we will takes extra spaces then time complexcity will be o(N)
ar=[1,2,3,4,5]
temp=ar[0]
for j in range(1,len(ar)):
    ar[j-1]=ar[j]
ar[len(ar)-1]  =temp 
print(ar)



