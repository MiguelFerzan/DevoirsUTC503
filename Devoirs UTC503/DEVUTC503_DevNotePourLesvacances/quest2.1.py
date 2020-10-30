#Version Recursive
def rendreMonnaie(listeMonnaies,sommeArendre):
    listeMonnaies.sort(reverse=True)
    if(len(listeMonnaies)==0):
        return[]
    else:
        return [sommeArendre//listeMonnaies[0],*rendreMonnaie(listeMonnaies[1:],sommeArendre%listeMonnaies[0])]


print(rendreMonnaie([5000,1000],7000))


