# Trouver le plus petit diviseur d’un nombre positif n
def ppd(n):
    if n < 1:
        return "Le nombre doit etre positif"
    else:
        for i in range(2,n+1): #on commence par 2 pour ne pas avoir toujours 1 comme reponse
            if n%i == 0:       #alors c'est le plus petit diviseur apres 1
                return i


print(ppd(36))

#on fait la division des des nombres de 2 a n+1
#on retourne le premier nombre qui le reste = 0
#car on cherche du plus petit au plus grand alors
#le premier nombre qui a le reste = 0 est le plus petit