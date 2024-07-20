# Majority elements  that will greater than n//3 times:
# So at  maximum 2 elements in entire arrays
# Brute force appraches o(n2) and o(1) will be the time complecity:
arr=[1,1,1,3,3,2,2,2]
lo=[]
n=8
for i in range(len(arr)):
    if len(lo)==0 or lo[0]!=arr[i]:
        count=0
        for j in range(len(arr)):
            if arr[j]==arr[i]:
                count+=1
        if count> n//3:
           lo.append(arr[i])     
    if len(lo)==2:
        break   
print(lo)        

# optimal solution:
