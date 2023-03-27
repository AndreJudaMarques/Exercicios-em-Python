''' ler ano de nascimento 7 pessoas, mostra quantas ja sao maiores, 
e quantas sao menores, maioridade  = 21  '''

#MINHA LINDA SOLUCAO

from datetime import date

anoAtual = date.today().year #confere ano atual

maior = []
contMaior = 0
menor = []
contMenor = 0

for c in range (1,8):
    ano = int(input('Digite o ano de nascimento com 4 digitos: '))
    if anoAtual - ano >= 21:
        maior.append(ano)
        contMaior += 1
    else:
        menor.append(ano)
        contMenor += 1
print()
print('Existem {} pessoas maiores: ' .format(contMaior))
print('As que nasceram em: {}' .format(maior))
    #se o ano(input)ex:1987 - anoatual = 2023 >= 21
    #maior recebe ano
    #conta 1
print()
print()
print('Existem {} pessoas menores: ' .format(contMenor))
print('As que nasceram em: {}' .format(menor))
print()