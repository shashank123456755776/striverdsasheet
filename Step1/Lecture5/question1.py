# understands recursions by print somethings N tIMES
# when a function called itself is called as functions:
# def fun():
#     fun()

# fun()
# This above code is example of recursions how function has been called inside another functions:
# Above function will gives stack overflow errors because their is no stop conditions:

# let use  suppose we wnat count upto 3 using recursions
count=1
def a():
    global count
    # bace case
    if count>20:
        return
    count+=1
    print(count)
    a()
   


a()    