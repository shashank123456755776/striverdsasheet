# # using two pinters pallindroem checks 
# found =True
# left=0
# n=16778
# n1=str(n)
# right=len(n1)-1
# while left<=right:
#     if n1[left]!=n1[right]:
#         found=False
#         break
#     elif  n1[left]==n1[right]:
#         found=True

#     left+=1
#     right-=1
# if not found:
#    print('we have no pallindrome numbers:')
# else:
#    print("we have pallindrome numbers:")      


#    by using extraction methods check pallindrome:n=1234
n2 = 121
reversed_num = 0
original_n2 = n2

while n2 > 0:
    n1 = n2 % 10
    reversed_num = (reversed_num * 10) + n1
    n2 = n2 // 10  # Integer division

if reversed_num == original_n2:
    print("Number is palindrome")
else:
    print("Number is not palindrome")
 

  





