# // please print  the extracted value from the last
# Striver Concepts Of Digits  ,How We get extract the digits of the numbers 
# Example 7789 %10==9 , Similary We can extracts the last digits like this 7%10 we get 7
n=int(input(" enter number:"))
while n>0:
    n1=n%10
    print(n1)
    n=n//10