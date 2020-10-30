#Version Iterative

def rendreMonnaie(listeMonnaies,sommeArendre):
    listeMonn=sorted(listeMonnaies, reverse=True)
    total=0
    i=0
    resultat=[]
    while total<sommeArendre:
        resultat.append(0)
        while total+listeMonnaies[i]<=sommeArendre:
            total+=listeMonnaies[i]
            resultat[i]=resultat[i]+1
        i=i+1
    return resultat

#on met dans la liste de monnaies les monnaies q'ont veut,et on peut mettre le nombre
#de monnaie q'ont veut(pas neccessairement 2,on peut mettre 3 ou 4 ou plus types de monnaie)
listeMonnaies=[5000,1000,250]
print(rendreMonnaie(listeMonnaies,12500))
    
#Si on a choisit les billets 5000 et 1000 et la piece 500, et la somme de retour
#est 7500, on rend 1 billet de 5000 et 2 billets de 1000 et une piece de 500
#alors le reultat qu'on le print est (1,2,1) par ordre

listeMonnaies2=[5000,1000]
print(rendreMonnaie(listeMonnaies2,7000))
