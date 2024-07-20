#Striver Sheet Pattern Questions 5
def mycode(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end="")
        for k in range(i):
            print(" " ,end=" ")
        print()        




n=5
mycode(n)  
