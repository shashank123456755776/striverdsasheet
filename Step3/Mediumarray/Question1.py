#2 Sum Problem means sum of two elements in array equla to array
# 1st variety,return indicies of both the numbers
target=14
ar=[2,6,5,8,11]
# brute force
def twosum():
    for i in range(len(ar)):
       for j in range(i+1,len(ar)):
           if ar[i]+ar[j]==target:
               return [i,j]
p=twosum()    
print(p)       

# Optimal Solutions:
# Time complexcity is o(N) ans space complexcity is o(1)
dic={}
def Twosum():
   for index,item in enumerate(ar):
       if target-item  not in dic:
          dic[item]=index
       else:
          return [dic[target-item],index]
q=Twosum()
print(q)       

# also could solve using two pointers:
# time complexcity is o(Nlogn)+o(N)
# space complexcity is o(1)
ar.sort()
left=0
right=len(ar)-1
while left<=right:
    if ar[left]+ar[right]>target:
        right-=1
    elif ar[left]+ar[right]<target:
        left+=1
    else:
      print([left,right])
      break



# 2nd variety,return yes or 
# similary to above varieties only we have return yes or no