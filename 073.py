'''tupla brasileirao'''
'''
a mostrar os 5 colocados 
b os ultimos 4
c uma lista em ordem alfabetica
d em que posicao esta chapecoense'''

print()
print('CAMPEONATO BRASILEIRO DE FUTEBOL')
print()

brasileirao = ('América-MG', 'Athletico-PR', 'Atlético-MG', 'Bahia', 'Botafogo', 
               'Bragantino', 'Corinthians', 'Coritiba', 'Cruzeiro', 'Cuiabá', 
               'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional',
               'Palmeiras', 'Santos', 'São Paulo', 'Vasco')

print(f'Aqui estão os {len(brasileirao)} times')
print()

print(brasileirao)
print()
print(f'Os 5 primeiros colocados são {brasileirao[:5]}')
print()
print(f'Os últimos 4 colocados são {brasileirao[-4:]}')
print()
print(f'Em ordem Alfabética fica assim {sorted(brasileirao)}')
print()
print('Digite o nome do time para saber sua posição: ')
time = input('--->: ').strip()
print()
print(f'O {time} está na posição {brasileirao.index(time)+1}')
print()

