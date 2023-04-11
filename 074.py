''' 5 numeros aleatorios numa tupla
mostrar maior e menor'''

from random import randint

numeros = []

cont = 0

while cont < 5:
    cont +=1 
    numeros.append(randint(0,9))

print()
print(numeros)
print()
print(f'O maior valor sorteado foi {max(numeros)}')
print()
print(f'O menor valor sorteado foi {min(numeros)}')
print()