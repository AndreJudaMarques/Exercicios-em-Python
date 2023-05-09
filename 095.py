nomes = []

golsLista = [] #esta lista vai ter a lista de gols de cada jogador

golsS = [] # esta lista tera todos os gols e sera copiada e limpa
''' [ [3,2],  [2,0,4],  [0,0,0,0] ]'''

totalLista = []
totall = []

cont = 0
partida = 1
total = 0

while True:
    print('---' * 15)
    nome = input('Nome do jogador: ')
    nomes.append(nome)
    qntsPartidas = int(input(f'Quantas partidas {nome} jogou? '))
    while cont < qntsPartidas:
        gols = int(input(f'Quantos gols na {partida}° partida ? '))
        total = total + gols
        golsS.append(gols)
        cont += 1
        partida += 1
    totall.append(total)
    totalLista.append(totall[:])
    golsLista.append(golsS[:])
    golsS.clear()
    totall.clear()
    continuar = input('Quer continuar? [S/N] ')
    cont = 0
    partida = 1
    total = 0
    if continuar in "nN":
        break
print('-=-' * 15)
print(f"{'cod':<4} {'nome':<15} {'gols':<15} {'total':<10}") #chat me ajudou a formatar o print abaixo
print('---' * 15)

for n, (nome, gols, total) in enumerate(zip(nomes, golsLista, totalLista)):
    print(f"{n:<4} {nome:<15} {str(gols):<15} {str(total[0]):<10}")

while True:
    print('---' * 15)
    mostrar = int(input('Mostrar dados de qual jogador? '))
    if mostrar == 999:
        print('Finalizando')
        break

    if mostrar > len(nomes):
        print(f'Erro! Não existe jogador com o código {mostrar}! Tente novamente')
  
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {nomes[mostrar]}')
        jogo = 1
        for i in golsLista[mostrar]:
            print(f'No jogo {jogo} fez {i} gols.')
            jogo += 1
        jogo = 1