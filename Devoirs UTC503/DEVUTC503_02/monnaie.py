class monnaie:
    def __init__(self,valeur,devise):
        self.valeur = valeur
        self.devise = devise


    def ajouter(self,monnaie):
        if(monnaie.devise != self.devise):
            raise TypeError("Differentes devises")
        else:
            self.valeur+=monnaie.valeur

    def retrancher(self,monnaie):
        if(monnaie.devise != self.devise):
            raise TypeError("Differentes devises")
        else:
            self.valeur-=monnaie.valeur


def test():
    m1=monnaie(5,"euro")
    m2=monnaie(7,"euro")
    m1.ajouter(m2)
    print(m1.valeur)

    m1=monnaie(5,"euro")
    m2=monnaie(7,"euro")
    m1.retrancher(m2)
    print(m1.valeur)

test();