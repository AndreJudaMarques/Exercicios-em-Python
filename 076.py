''' tupla unica
nome produtos e preços na sequencia
listagem de precos'''

listagem = ('Pão', 1.00, 'Leite', 3.50, 'Frango', 10.90, 'Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90 )

print()
print('---' * 10)
print('      Listagem de Preços')
print('---' * 10)

cont = -1   
#while cont < 11:
for iten in listagem:
    cont += 1
    print(f'{listagem[cont]}............R$  {listagem[cont+1]}')
    cont += 1
print('---' * 10)
print()



'''for iten in listagem:
    print()
    print('---' * 10)
    print('      Listagem de Preços')
    print('---' * 10)
    print(f'{listagem[0]}............R$   {listagem[1]}')
    print(f'{listagem[2]}..........R$   {listagem[3]}')
    print(f'{listagem[4]}............R$   {listagem[5]}')
    print(f'{listagem[6]}............R$   {listagem[7]}')
    print(f'{listagem[8]}............R$   {listagem[9]}')
    print(f'{listagem[10]}............R$   {listagem[11]}')
    print()'''
