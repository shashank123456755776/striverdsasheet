#Striver Sheet Pattern Questions 6
def mycode(n):
    for i in range(n):
        for j in range(n-i):
            print(j+1,end="")
        for k in range(i):
            print(" " ,end=" ")
        print()        




n=5
mycode(n)  
