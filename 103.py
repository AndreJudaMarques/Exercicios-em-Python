def ficha(nome="desconhecido"):
     print('---' * 15)
     nome = input('Digite o nome do jogador: ')
     if not nome:
          nome = '<desconhecido>'
     gols = input('Digite a quantidade de gols: ')
     if not gols:
          gols = 0
     print(f'---> O jogador {nome} fez {gols} gols(s) na partida')
     print()

ficha()
