'''ler ano nascimento de um jovem
se ainda vai ter que se alistar
se esta na hora de se alistar
ja passou do tempo de se alistar

tambem quanto tempo falta ou passou do prazo'''

print('-=-' * 12)
print('Programa que verifica prazo de alistamento para o exército ')
print('-=-' * 12)

nome = input('Digite seu nome: ')
dataDeNascimento = int(input('Digite o ano de nascimento com 4 dígitos: '))
print()

from datetime import date

anoAtual = date.today().year #confere ano atual da maquina

''' anoAtual - dataDeNascimento = idade '''

idade = anoAtual - dataDeNascimento

if idade < 18:
    print('Você terá que se alistar em {} anos. ' .format(18 - idade))

elif idade == 18:
    print('Está na hora de se alistar!\ncompareça a o exército para se alistar neste ano. ')

else:
    print('Já passou o seu tempo de se alistar!. ')

print()