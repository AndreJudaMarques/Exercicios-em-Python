''' adivinhar numero 1-10, tentar ate acertar
mostrar quantidade tentativas'''

from random import randint

from time import sleep

numeroPC = randint(1,10)

#print(numeroPC) teste

print('-_-' * 10)
print('Bem vindo ao Jogo de Adivinhar! ')
print()
sleep(2)
print('Vou adivinhar um número de 1 a 10 e você tentará adivinhar ok?!')
#y sim n nao
print()
sleep(2)
print('Vamos começar! ')
sleep(1)
print()
print('Estou pensando em um número')
sleep(2)
print('pensando.....')
sleep(3)
print()
print('Escolhi, agora tente adivinhar 1-10:')

numero = int(input())
cont = 1

while numero != numeroPC:
    print('Errou! tente novamente. ')
    numero = int(input())
    cont += 1
    if numero == numeroPC:
        print('Acertou! o número escolhido foi o {} e você acertou em {} tentativas ' .format(numero, cont))
        break
print()
parar = input('Digite qualquer coisa para sair...')
print()

''' enquanto numero digitado for diferente numeroPC
tente novamente
conta tentativas'''
