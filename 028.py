#computador pensar entre 0 e 5
#tentar adivinhar
#print venceu ou perdeu

#import random

#minha solucao

from random import randint

numero = int(input('Adivinhe um número entre 1 e 5: '))

r = randint(1,5)

if numero == r:
    print('Você acertou! o número sorteado é {}' .format(r))
else:
    print('Você errou!')