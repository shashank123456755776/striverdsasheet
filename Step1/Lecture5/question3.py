# sum of n naturals numbers:
# two solve this problems their is two ways paramaterized ways and the second way is functional ways
# lets solve by first parameterized methods:;
# this has ben used when we need to print somathing 

def parasum(i,sum):
    if i<1:
        print(sum)
        return
    parasum(i-1,sum+i)
parasum(3,0)    

# when we wants to return the valuse the we would used functional ways
def fact(s):
    if s == 0:
        return 1
    return s * fact(s - 1)

result = fact(5)
print(result)  # Output: 120

# factorial programms using recursions:
def fact(s):
    if s==0:
        return 1
    return s*fact(s-1)
fact(5)    


# sum with parametrized methods:
def sums(i,sum):
    if i<1:
        print(sum)
        return 
    sums(i-1,sum+i)
k=3
sums(k,0)    
#functional methods 
def mysums(i):
    if i == 0:
        return 0
    return i + mysums(i - 1)

print(mysums(3))


# factorials of a numbers:this is a functional methods
def fact(a):
    if a==1:
      return 1
    return a*fact(a-1)

a=5
print(fact(a))    
