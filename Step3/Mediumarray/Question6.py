# Rearrange the array in alternating postive and negative items:
# Rearrange elemnets by sign but order should be maintain like +,-+,-
# Equal postive and negative numbers:
# Means if n=8 then n/2 negative and n/2 positive number:

# Brute force Method
# Time Complexcity  is o(2N) and space complexcity is o(N/2)+o(N/2)=o(N)
negative=[]
positive=[]
ar=[3,1,-2,-5,2,-4]
for i in range(len(ar)):
    if ar[i]<0:
        negative.append(ar[i])
    elif ar[i]>0:
        positive.append(ar[i])    
for j in range(len(ar)//2):   
    ar[2*j]=positive[j]     
    ar[2*j+1]=negative[j] 
print(ar)    
# Optimal Solution 
# Time complexcity is o(N) and space is 0(1)
ar = [3, 1, -2, -5, 2, -4]
n = [0] * len(ar)  # Initialize n with zeros

positive_index = 0
negative_index = 1

for num in ar:
    if num > 0:
        n[positive_index] = num
        positive_index += 2
    else:
        n[negative_index] = num
        negative_index += 2

print(n)

# All above Problems for number of postive equal to negative numbers:

# now case what happen if number of postive numbers and negative numbers will not equal:
# brute force
# time will be o(2N) and space complexcity will be 0(N)
ar=[-1,2,3,4,-3,1]
po=[]
ne=[]
s=2
for i in range(len(ar)):
    if ar[i]>0:
        po.append(ar[i])
    else:
        ne.append(ar[i])  
for j in range(len(ne)):
    ar[2*j]=po[j]
    ar[2*j+1]=ne[j] 
print(ar)    
for k in range(2*len(ne),len(ar))  :
    ar[k]=po[s]
    s+=1  
print(ar)           


