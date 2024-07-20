# def rever(n1):
#     s=n1[::-1]
#     return int(s)
# n=123
# n1=str(n)
# print(rever(n1) )   
# lets reverse the number using extarction concepts:
# so in such case we can calculate the reverse the reverse number:
#  formula reverse=(reverse*10)+lstdigit whre reverse=0
n=1234
re=0
while n>0:
    n1=n%10
    re=(re*10)+n1
    n=n//10
print(re)    
   
   