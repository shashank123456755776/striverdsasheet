# pascal triangle
# tree types of the problems:
# 1 given R and C ,tell me elements at that place r=5,c=3
# 2 print nth row of the pascal triangle:
# 3 print entire pascal triangle:

# 1 question;
# Brute Force:
# Formula 
# r-1 C c-1 =r-1!/r!*(n-(r-1))= 24/2*2=6
# it will takes time o(n)+o(n-r)+o(r)
# lets optimized
# 10C3 =10*9*8/3*2*1
# accordingly
# optimal solution  of first type questions:
# time complexcity o(r) and space complecity o(1)
n=4
r=3
def ncr(n,r):
    res=1
    for i in range(r):
        res=res*(n-i)
        res=res//(i+1)
    return res
print(ncr(n,r)) 

# print any row :
# nth row has n elelmnts:
# brute force:
# time complexcity will be o(n*r)
for c in range(0,r):
    print(ncr(n-1,c))
# optimized
# we will optimized  formula with zero indices means 5c0,5c1
# we will making formula in this code:
# time complecity will be o(n)
ans = 1

print(ans)  #

for i in range(1, n):  # Loop from 1 to n-1
    ans = ans * (n - i)
    ans = ans // i
    print(ans) 


# 3rd questions:
# brute approaches to print pascal triangles:
ans = []
n = 6

def ncr(n, r):
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res

for row in range(n):
    temp = []
    for col in range(row + 1):
        temp.append(ncr(row, col))
    ans.append(temp)

print(ans)
# but above code it will takes o(n3) time 
# By  using Second type We  can optimized
n = 5
ans = 1
bo = []

def fun(n, ans):
    row = [1]
    for i in range(1, n):
        ans = ans * (n - i)
        ans = ans // i
        row.append(ans)
    return row

for j in range(1, n + 1):
    p = fun(j, ans)
    bo.append(p)

print(bo)



