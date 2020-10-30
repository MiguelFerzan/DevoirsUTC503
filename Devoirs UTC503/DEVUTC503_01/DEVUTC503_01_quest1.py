#iteratif
def facItr(n):
    
    if n < 0:
        return("Le nombre ne peut pas etre negative")
        
    if n == 0 or n == 1:
        return 1
        
    if n > 1:
        res = n
        n1 = n
        while(n1 > 1):
            n1 = n1 - 1
            res = res * n1
    return res

def facRec(n):
    if n < 0:
        return("Le nombre ne peut pas etre negative")

    if n == 0 or n == 1:
        res = 1

    if n > 1:
        res = n * facRec(n-1)
    return res

print(facItr(7))
print(facRec(7))

