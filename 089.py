'''ler nome e 2 notas de varios alunos
guardar tudo lista composta'''

''' listona
dentro dela uma lista menor
e dentro outra lista menor'''

''' mostrar boletim contendo a mediade de cada um 
e permita que o usuario possa mostrar as notas individualmente'''
from time import sleep

boletim = []

alunos = []

nomes = []

medias = []

cont = 0
while True:
    nome = input('Nome: ')
    alunos.append(nome)
    nomes.append(nome)
    n1 = float(input('Nota 1: '))
    alunos.append(n1)
    n2 = float(input('Nota 2: '))
    alunos.append(n2)
    media = (n1 + n2) / 2
    medias.append(media)
    media = 0
    boletim.insert(cont, alunos[:])
    cont += 1
    alunos.clear()
    continuar = input('Quer continuar?[S/N]: ').lower()
    if continuar == 'n':
        break
print(boletim)

print('-=-' * 8 )
print('Nº. Nome       Média')
print('---' * 9)
cont = 0
for pos, n  in enumerate(nomes):
    print(f'{pos}   {n}      {medias[cont]}')
    cont+= 1
print('---' * 9)

while True:
    NumeroDoAluno = int(input('Digite o Número° do aluno para mostrar suas notas ou 999 para PARAR: '))
    if NumeroDoAluno == 999:
        break
    print(f'As notas de {boletim[NumeroDoAluno][0]} são {boletim[NumeroDoAluno][1:3]}') 
    print('---' * 9)

print('FINALIZANDO...')
sleep(1)
print('<<< VOLTE SEMPRE >>>')
enter = input('Tecle ENTER para sair... ')