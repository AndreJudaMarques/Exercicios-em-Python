from random import randint
from time import sleep
from operator import itemgetter

dici = { }
print('Valores sorteados: ')
for j in range(0,4):
    n = randint(0,6)
    print(f'   O jogador {j+1} tirou {n}')
    #sleep(1)
    dici[f'jogador{j+1}'] = n
# minha solucao ate aqui, o restante abaixo tive que tirar do video pois ele nao tinha ensinado
#o itemgetter

ranking = list()
ranking = sorted(dici.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores: ')
for i, v in enumerate(ranking):
    print(f'    {i+1}º Lugar:  {v[ 0]} com {v[1]}')
    sleep(1)