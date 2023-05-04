dici = {}
golslista = []

nome = input('Nome do jogador: ')
qntdPartidas = int(input(f'Quantas partidas {nome} jogou? '))

dici['nome'] = nome

cont = 1
total = 0
while cont <=qntdPartidas:
    partida = int(input(f'Quantos gols na partida {cont}? '))
    golslista.append(partida)
    total = total + partida
    cont += 1
dici['gols'] = golslista
dici['total'] = total
print('-=-' * 10)
print(dici)
print('-=-' * 10)

for k, v in dici.items(): #para cada chave(keys) e valor(values) no dicionario
    print(f'O campo {k} tem o valor {v}.')
print('-=-' * 10)
print(f'O jogador {nome} jogou {qntdPartidas} partidas.')

cont2 = 1
gole = 0
while cont2 <=len(golslista):
    print(f'{f"=> Na partida {cont2}, fez {golslista[gole]} gols.":>35}') 
    cont2 += 1
    gole += 1
print(f'Foi um total de {total} gols')
print()
