#equation premier degre
def premierDegre(a,b):
    '''
       Solution équation premier degré ax+b=0

       :param a: coéficient de x
       :param b: constatnte
       :result: -b/a si a non nul,
                 a et b nul infinité de solution
                 a nul b non nul pas de dolution
    '''
    if a == 0:
        if b==0:
            return "Infinité de solutions"
        else:
            return "Impossible pas de solutions"
    else:
        return premDegreAnonNul(a,b)

# premDegre calcul -b/a a condition d'être sure que a!=0
def premDegreAnonNul(a,b):
    '''
       Solution équation premier degré ax+b=0

       :param a: coéficient de x a non nul
       :param b: constatnte
       :result: -b/a
    '''
    # assert permet de faire de la programation deffensive
    assert a!=0,"A ne doit pas être nul"
    return -b/a

#test et exemples
if __name__ == '__main__':
    assert(premierDegre(0,0)) == "Infinité de solutions"
    print(premierDegre(0,0))
    assert(premierDegre(0,1)) == "Impossible pas de solutions"
    print(premierDegre(0,1))
    assert(premierDegre(1,-1)) == 1
    print(premierDegre(1,-1))


#equation second degre
def delta(a,b,c):
    return b * b - 4 * a * c

def secDeg(a,b,c):
    if (a == 0): return premierDegre(b,c)
    else:
        delta1 = delta(a,b,c)
        if (delta1 > 0): 
            da= 2 * a
            return ((-b - delta1**0.5)/da,(-b + delta1**0.5)/da)
        elif delta1 < 0:
            return "Pas de solutions"
        else: return -b/2*a



