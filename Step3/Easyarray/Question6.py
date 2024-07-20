#Left rotate an array by D places:
#In such problem two cases first cases d<len(ar) and d>len(ar)
# here time complexcity is o(N+d) and space complexcity is o(d)
# brute force approaches
temp = []
d = 3
ar = [1, 2, 3, 4, 5, 6, 7]
def rotation(ar,d):
  if d<len(ar):
     for i in range(d):
         temp.append(ar[i])
     for i in range(d, len(ar)):
         ar[i - d] = ar[i]
     for i in range(len(ar) - d, len(ar)):
         ar[i] = temp[i - (len(ar) - d)]
  else:
      d=d%len(ar)     


rotation(ar,d)
print(ar)

# Optimal approaches with o(1) space space complexcity but time(2n)
# python compliers 
ar=[1,2,3,4,5,6,7,8]
d=3
def reverse(ar,start,end):
   while start<=end:
       ar[start],ar[end]=ar[end],ar[start]
       start+=1
       end-=1
def rotatearrays(ar):
    reverse(ar,0,d-1)
    reverse(ar,d,len(ar)-1)
    ar.reverse()
    return ar
print(rotatearrays(ar))   



