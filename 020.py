#sortear a ordem de apresentacao de trabalho dos alunos, ler o nome dos 4 alunos
# mostrar a ordem sorteada

import random

n1 = input(' Digite o nome do 1º aluno: ')
n2 = input(' Digite o nome do 2º aluno: ')
n3 = input(' Digite o nome do 3º aluno: ')
n4 = input(' Digite o nome do 4º aluno: ')

lista = [n1, n2, n3, n4]

random.shuffle(lista) # embaralha a list

print(' A ordem de apresentação será: \n', lista)