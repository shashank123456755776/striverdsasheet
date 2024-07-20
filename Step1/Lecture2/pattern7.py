#Striver Sheet Pattern Questions 7
def mycode(n):
    for i in range(n):
        for j in range(n-1-i):
            print(" ",end=" ")
        for k in range(2*i+1):
            print("*" ,end=" ")
        print()        




n=5
mycode(n)  
