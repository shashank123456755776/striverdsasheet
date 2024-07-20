#Longest Consecutive Sequence  in an Array:
ar=[102,4,100,1,101,3,2,1,1]
# Brute force: 
# It will takes o(n2) Time Complexsity
lo=0
for i in range(len(ar)):
    x=ar[i]+1
    count=1
    while  x in ar:
        count+=1
        x=x+1
        
    lo=max(lo,count) 
print(lo)       
#Better approaches  Approaches:
# in sorting the time complexcity will be o(Nlogn)+o(N)
ar = [102, 4, 100, 1, 101, 3, 2, 1, 1]
ar.sort()  # Sort the array first
nex = 0
longest = 0
count = 1

for i in range(len(ar) - 1):
    if ar[i + 1] != ar[i] and abs(ar[i + 1] - ar[i]) == 1:
        count += 1
    else:
        longest = max(longest, count)
        count = 1  # Reset count when consecutive sequence ends
print(longest)
# optimal solution
# time compplexcity is o(N+M)=o(3N)
# space complexcity is o(N)
p = set(ar)
start = 0
longest = 0
count = 1  

for ele in p:
    if ele - 1 not in p:
        start = ele
        while start + 1 in p:
            count += 1
            start += 1
        longest = max(longest, count)
        count = 1  # Reset count for the next sequence

print(longest)

       