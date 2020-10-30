#1.Nombre des elements
def recursiveListNum(list):
    total=0
    for element in list:
        if type(element)==type([]):
            total+=1
            recursiveListSum(element)
        else:
            total+=1
    return total
print(recursiveListNum([20,3,12,5]))

#2.Somme des elements
def recursiveListSum(list):
    total=0
    for element in list:
        if type(element)==type([]):
            total=total+recursiveListSum(element)
        else:
            total=total+element
    return total

print(recursiveListSum([20,3,12,5]))

#3.Moyenne des éléments d’une séquence numérique
def recursiveListMoy(list): #Version dans la quelle on appelle les 2 fonctions
    res1=recursiveListSum(list)    #deja ecrites dans les questions 1 et 2
    res2=recursiveListNum(list)
    return res1/res2

print(recursiveListMoy([20,3,12,5]))

def recursiveListMoy2(list):  #Version dans la quelle on a implementer les 2 fonctions
    total=0          #deja ecrites dans les quest 1 et 2 pour creer une fonction
    total2=0         #qui est actuellement recursive au lieu d'appeler des fonctions
    for element in list:
        if type(element)==type([]):
            total=total+recursiveListSum(element)
            total2+=1
        else:
            total=total+element
            total2+=1
    return total/total2

print(recursiveListMoy2([20,3,12,5]))


#4.Insérer un élément dans une liste trié

def insert(lst, to_insert, left=0, right=None):
    if right is None:
        right = len(lst)

    if left == right:
        return lst[:left] + [to_insert] + lst[left:]

    else:
        mid = left + (right-left) // 2
        if lst[mid] == to_insert:
            left = right = mid
        elif lst[mid] < to_insert:
            left = mid + 1
        else:
            right = mid
        # move left or right, then
        return insert(lst, to_insert, left, right)
print(insert([1,3,5,7],4))

#5.Tri d’une liste
def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        return quick_sort([e for e in l[1:] if e <= l[0]]) + [l[0]] +\
            quick_sort([e for e in l[1:] if e > l[0]])

print(quick_sort([5,3,7,1,10]))