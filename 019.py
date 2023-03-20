#sortear um aluno para apagar o quadro. faça um programa que le o nome dos alunos e escreva o escolhido

import random

#posso fazer from random import choice

print(' Sorteio de 4 Alunos ')

nome1 = input(' Digite o nome do 1º aluno: ')
nome2 = input(' Digite o nome do 2º aluno: ')
nome3 = input(' Digite o nome do 3º aluno: ')
nome4 = input(' Digite o nome do 4º aluno: ')

lista = [nome1, nome2, nome3, nome4]


print(' O aluno escolhido foi {} ' .format(random.choices(lista)))

# se usar from random import o print fica:
#.format(choices(lista)

#escolhido = random.choice(lista) variavel com o escolhido, aqui o random escolhe antes do print

