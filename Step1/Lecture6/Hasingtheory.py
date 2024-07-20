# Hashing
# prestoring/fetching
ar=[1,2,3,3,1,1,1,4,3,4]
dic={}
for i,num in enumerate(ar):
    if num not in dic:
        dic[num]=1
    else:
        dic[num]+=1
print(dic)      
print(dic.items())
# print(dic.keys())
# print(dic.values()) 
# which is highest frquency and which is lowest frequencies 
print(max(dic.items()))
print(min(dic.items()))

    
