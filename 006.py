import math
numero = int(input(' Digite um numero: '))

raiz = math.sqrt(numero) #raiz = n ** (1/2)

print('O dobro do seu número é: {} \n O triplo do seu número é {} \n e a raiz quadrada é {:.2f}. ' .format(numero *2, numero*3, raiz))