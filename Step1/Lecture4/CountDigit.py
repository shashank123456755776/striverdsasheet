# def counts(n1):
#     count=0
#     for i in range(len(n1)):
#         count+=1
#     return count    
# n=23627
# n1=str(n)
# print(counts(n1))      
# Count the digits by extracted methods : 2nd metods 

n=1345
# time complexcity 0(log10(N)) depends upon divisible by 10 or 5 0r any
# if number of iterations depends upon divisions then time compleciyt depends into pictures
def count(n):
  count1=0
  while n>0:
     n1= n%10
     count1+=1
     n=n/10
  return count1   
print(count(n))
# By Using Logarithom Operation We can also used the concepts
