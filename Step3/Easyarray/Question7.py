# Moves zeros to the end of the arrays
# brute forces
# time complexcity is o(N)+o(n-x)+o(x)=o(2N) and space complexcity is o(N)
ar = [1, 0, 2, 3, 4, 0, 0, 4, 5, 6, 0, 8, 9,0,0,0,7]

temp = []
for i in range(len(ar)):
    if ar[i] != 0:
        temp.append(ar[i])
for j in range(len(temp)):
    ar[j] = temp[j]

for k in range(len(temp), len(ar)):
    ar[k] = 0
print(ar)

# optimal approaches using two pointers 
# time complexcity is o(N) and space complex is o(1)
krishna=0
Radha=1
for i in range(len(ar)-1):
    if ar[i] ==0 and ar[i+1]==0:
        Radha+=1 
    if ar[i]==0 and ar[i+1]!=0:
        ar[i],ar[i+1],ar[i+1],ar[i]
    krishna+=1
    Radha+=1
   
print(ar)        

