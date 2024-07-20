# Multiple Recursions calls 
# nth fibonacci number in  fibonacci series:
n=4
def fib(n):
    if n<=1:
        return n
    l=fib(n-1)
    r=fib(n-2)
    return l+r
print(fib(n) )   
# to analyze write the recursion tree