import math #modulo importa funcoes da biblioteca MATH

# se quiser so a funcao sqrt( raiz quadrada)
# pode ser from math import sqrt
# pode ser from math import sqrt, floor ; outro exemplo

num = int(input(' Digite um numero: '))

raiz = math.sqrt(num)

print(' A raiz de {} é igual a {} ' .format(num, raiz)) 

#.format(num, math.ceil(raiz)) faz o arredondamento para cima

print(' A raiz de {} é igual a {} ' .format(num, math.ceil(raiz))) 

print(' A raiz de {} é igual a {} ' .format(num, math.floor(raiz))) #arredondamento para baixo

import emoji # para instalar a biblioteca digitei pip install emoji no terminal do vscode aqui mesmo

#print(emoji.emojize(' Ola mundo :sunglasses:', use_aliases=True))


