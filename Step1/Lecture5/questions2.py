#Print name n time using recursion:
# by using paramaterizied methods 
# why paramaterizied because no global varibale has been used
# time complexcity will be o(n) and space complexcity will be o(n)
def name(i,n):
    if i>n:
        return
    print('krishn and radharani')
    name(i+1,n)
n=10
name(1,n)    

# print 1-n
def num(i,n):
    if i>n:
        return
    print(i)
    num(i+1,n)


num(1,n)    

# print n-1
def nums(i,n1):

    if i==n1:
       return
    print(n1-i)
    nums(i+1,n1) 


 
n1=20
nums(1,n1)    

# print 1-n using backtracking
# here very  important concepts is called backtracking ,where ecah function called until wde meet bace cases loops goings on
# when function return where it has been called then it will starts printing the numbers
def back(i,n):
    if i<1:
      return
    back(i-1,n)
    print(i)
p=5
back(p,p)      
# so here whether we starts from n=3 but it will print linearly

  
# print n-1 using backtracking
def back1(i,s):
    if i>s:
        return
    back1(i+1,s)
    print(i)
    # output will be 3,2,1
s=3
back1(1,s)    



