''' jogar par ou impar com pc
so sera interrompido quando player perder
mostrando total de vitorias
'''
from random import randint

print('=-=' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR ')
print('=-=' * 10)

numero = int(input('Diga um valor: '))

escolha = input('Par ou Ímpar? [P/I]: ').upper()
print('-' * 20)

pc = randint(1,5) # pc escolhendo entre 1 e 2

total = numero + pc

if total % 2 == 0:
    jogo = 'P'
    game = 'PAR'
else:
    jogo = 'I'
    game = 'ÍMPAR'

cont = 0
while escolha == jogo:
    print(f'Você jogou {numero} e o computador {pc}. Total de {total} DEU {game} ')
    print('Você VENCEU! \nVamos jogar novamente...  ')
    print('-' * 20)
    cont += 1
    numero = int(input('Diga um valor: '))
    escolha = input('Par ou Ímpar? [P/I]: ').upper()
    print('-' * 20)
    pc = randint(1,5) # pc escolhendo entre 1 e 2
    #print(pc)
    total = numero + pc
    if total % 2 == 0:
        jogo = 'P'
        game = 'PAR'
    else:
        jogo = 'I'
        game = 'ÍMPAR'

print(f'Você jogou {numero} e o computador {pc}. Total de {total} DEU {game} ')
print('Você PERDEU!')
print(f'GAME OVER! Você venceu {cont} vezes. ')
print('-' * 20)
sair = input('Digite qualquer coisa pra sair ...')
print()


