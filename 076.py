''' tupla unica
nome produtos e preços na sequencia
listagem de precos'''

listagem = ('Pão', 1.00, 'Leite', 3.50, 'Frango', 10.90, 'Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90 )

print()
print('---' * 13)
print(f'{"Listagem de Preços":^40}') #40 espaços centralizados
print('---' * 13)
#MINHA SOLUCAO ABAIXO
'''cont = 0   
while cont < len(listagem)-1:
#for iten in listagem:
    #cont += 1
    print(f'{listagem[cont]}............R$  {listagem[cont+1]}')
    cont += 1
print('---' * 10)
print()'''

#solucao video abaixo:
# pos =  posicao
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='') #pontos alinhados a esquerda :.<30
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('---' * 13)

print()

