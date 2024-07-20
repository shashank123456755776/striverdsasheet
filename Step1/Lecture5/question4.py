#  reverse an arrays using recursion using two pointers

arr=[1,2,3,4,5]
r=len(arr)-1
l=0
def rev(l,r):
    if l>=r:
        return arr
    arr[l],arr[r]=arr[r],arr[l]
    return rev(l+1,r-1)

print(rev(l,r))

#another methods of swapping :
ar=[1,3,4,5,6]
n=len(ar)
def rev1(i):
   
      if i>=n/2:
           return ar
        
      ar[i],ar[n-i-1]=ar[n-i-1],ar[i]
      return rev1(i+1)

print(rev1(0))
# single recursions calls:


# check given strings is pallindroem or not using recusions:
string="abba"
def pallindrome(i):
     n=len(string)
     if i>=n/2:
          return True
     if string[i]!=string[n-i-1]:
          return False
     return pallindrome(i+1)
     
      
print(pallindrome(0) )    