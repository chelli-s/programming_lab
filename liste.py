def stampa(lista):
    if not isinstance(lista,list):
        raise Exception('L input non e una lista')
    return lista

def statistiche(lista):
    somma=0
    for item in lista:
        if not isinstance(item,int):
            lista=[]
            return lista
    for item in lista:
        somma+=item
    media=somma/len(lista)
    min=lista[0]
    for item in lista:
        if min>item:
            min=item
    max=lista[0]
    for item in lista:
        if max<item:
            max=item
    
    return 'somma= {} media= {} min= {} max= {}'.format(somma,media,min,max)

def somma_vettoriale(lista1,lista2):
    for item in lista1:
        if not isinstance(item,int):
            raise Exception('non-integer value not supported')
    for item in lista2:
        if not isinstance(item,int):
            raise Exception('non-integer value not supported')
    if len(lista1)==len(lista2):
        for i in range(0, len(lista1)):
            lista1[i]+=lista2[i]
        return lista1
    else:
        lista=[]
        return lista

def prodotto_vettoriale(lista1,lista2):
    for item in lista1:
        if not isinstance(item,int):
            raise Exception('non-integer value not supported')
    for item in lista2:
        if not isinstance(item,int):
            raise Exception('non-integer value not supported')
    if len(lista1)==len(lista2):
        for i in range(0, len(lista1)):
            lista1[i]*=lista2[i]
        return lista1
    else:
        lista=[]
        return lista


print(stampa([2,3,87]))
print(statistiche([2,3,87]))
print(somma_vettoriale([2,3,87] , [1,5,7]))
print(prodotto_vettoriale([2,3,87] , [1,5,7]))