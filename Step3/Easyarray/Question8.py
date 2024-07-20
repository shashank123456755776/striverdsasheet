# Linear Search
target =9
ar=[1,2,4,45,5,68,9,11,131,14]
def linear(ar):
  for i in range(len(ar)):
      if ar[i]==target:
        return True
        break
     
  return -1
print(linear(ar)) 
