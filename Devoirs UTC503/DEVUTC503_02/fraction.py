class fraction:
    def __init__(self,numerateur,denominateur):
        self.numerateur = numerateur
        self.denominateur = denominateur

    def __add__(self,other):
        pass
    def __mult__(self,other):
        pass

    def decompose(n): 
        res=[]
        i=2 
        while n>1: 
            while n%i==0: 
                res += [i]
                n=n/i 
            i=i+1 
        return res

    def simplifie(self):
        num=fraction.decompose(self.numerateur)
        den=fraction.decompose(self.denominateur)
        num1=num[-1]
        den1=den[-1]
        self.numerateur=num1
        self.denominateur=den1

    

f1=fraction(12,8)
print(f1.numerateur, f1.denominateur)
f1.simplifie()
print(f1.numerateur, f1.denominateur)