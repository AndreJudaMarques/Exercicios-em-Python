from random import randint

lista = []

def sort():
    cont = 0
    while cont < 5:
        num = randint(1,9)
        lista.append(num)
        cont+=1 

def par():
    pares = 0
    for i in lista:
        if i % 2 == 0:
            pares = pares + i
    return(pares)

sort()
par()
print()
print(f'Sorteando 5 valores da lista: {lista}')
print(f'Somando os valores pares de {lista}, temos {par()}')
print()