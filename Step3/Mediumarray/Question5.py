# Best Time to buy and Sell  such that profit should be the maximum:
# Optimal approaches using two pointers:
# Time complexcity is o(N) which is most optimal
arr=[7,1,5,3,10,4]
i=0
j=1
profit=0
while j <len(arr):
    if arr[i]>arr[j]:
        i+=1
        j+=1
    elif arr[j]>arr[i]:
        maxi=arr[j]-arr[i]
        profit=max(profit,maxi)
        j+=1 
    else:
        i+=1
        j+=1      
print(profit)        



