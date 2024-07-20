# let using map function to run cube function on each func tion 

n=1234
n2=n
sum=0
while n>0:
    n1=n%10
    sum=(sum+n1**3)
    n=n//10
if sum==n2:
    print("amestrong numbers")
else:
    print("not amestrongs numbers:")    