# Recusion in insertion sorts 
def sorti(ar, i):
    if i <= 0:
        return

    if ar[i] < ar[i - 1]:
        ar[i], ar[i - 1] = ar[i - 1], ar[i]
        i-=1
        sorti(ar, i ) 
    else:
        return

def insertionrec(ar, n, i):
    if i >= n:
        return
    
    sorti(ar, i)  
    
    i+=1
    insertionrec(ar, n, i ) 


ar = [13,10,86,0,-1,3]
insertionrec(ar, len(ar), 1)  
print(ar)
