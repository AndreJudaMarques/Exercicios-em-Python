''' mostrar fatorial numero 
5! = 5x4 5x3 5x2 5x 1 = 120'''

print('Digite um numero para verificar seu fatorial !')

numero = int(input('--->: '))

resultado = 0
cont = 0

while cont != 1:
    cont = numero -1 
    resultado = numero * cont
    cont -= 1
    while cont != 1:
        resultado = resultado * cont
        cont -= 1

print('O fatorial de {}! é {} ' .format(numero, resultado))
        
''' fatorial de 5:
fat cont resultado
5 - 1 = 4
5 x 4 = 20 
----
cont -1 = 3
resultado x 3 = 60

cont -1 = 2

resultado x 2 = 120

cont -1 = 1'''