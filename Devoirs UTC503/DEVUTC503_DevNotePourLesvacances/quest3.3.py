#Version Iterative
def toutRendreMonnaie(listeMonnaies,sommeArendre):
    listeMonn=sorted(listeMonnaies, reverse=True)
    total=0
    i=0
    resultat=[]
    resultat2=[]
    while total<sommeArendre:
        resultat.append(0)
        while total+listeMonnaies[i]<=sommeArendre:
            total+=listeMonnaies[i]
            resultat[i]=resultat[i]+1
        i=i+1
    total=0
    i=0

    for x in listeMonnaies:
        resultat2.append(0)
        if sommeArendre%listeMonnaies[i]==0:
            resultat2[i]=sommeArendre//listeMonnaies[i]

        i=i+1
    return resultat,resultat2

listeMonnaie=[5000,1000]
print(toutRendreMonnaie(listeMonnaie,7000))