''' ler um ano e mostrar se é bissexto
0 para ano atual
'''

from datetime import date

#solucao video

ano = int(input(' Que ano quer analisar? '))

if ano == 0:
    ano = date.today().year #confere ano atual da maquina

if ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0:
    print(' O ano {} é BISSEXTO ' .format(ano))
else:
    print(' O ano {} NÂO é BISSEXTO ' .format(ano))