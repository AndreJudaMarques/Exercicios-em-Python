
#crie um um programa que leia um numero real e mostre a sua porção inteira

# import math para todas as funcoes da biblioteca

from math import trunc #importou apenas 1 funcao da biblioteca

numero = float(input(' Digite um numero: '))

print(' A porção inteira do número é {} !' .format(trunc(numero)))

#.format(math.trunc(numero) se eu tivesse importado a biblioteca toda

