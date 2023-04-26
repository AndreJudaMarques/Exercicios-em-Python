'''cadastrar pessoas com nome e peso
dizer quntas tem na lista
os maiores pesos 100 kgs
os menores pesos 70 kgs'''

# minha solucao abaixo
'''pessoas = list()

dados = list()

maior = []
menor = []

cont = 0

while True:
    nome = str(input('Nome: '))
    dados.append(nome)
    peso = int(input('Peso: '))
    dados.append(peso)
    pessoas.append(dados[cont:])
    cont +=2 
    continuar = input('Quer continuar? [S/N]: ').upper()
    if continuar == 'N':
        break

for pessoa in pessoas:
    if pessoa[1] >= 100:
        maior.append(pessoa)

for pessoa in pessoas: 
    if pessoa[1] <= 70:
        menor.append(pessoa)
print()

print(f'Você cadastrou {len(pessoas)} pessoas ')
print(f'O maior peso foi de 100kg. Peso de', end=' ')
for pessoa in maior:
    print(f'{pessoa[0]}', end=' ')
print(f'\nO menor peso foi de 70kg. Peso de', end=' ')
for pessoa in menor:
    print(f'{pessoa[0]}', end=' ')'''


#solucao video abaixo

temp = [] #lista temporaria
princ = [] #lista principal
maior = menor = 0

while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:]) #dessa maneira cria uma copia nao uma ligacao
    temp.clear()
    resp = input('Quer continuar ? S/N ')
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Os dados foram {princ}')
print(f'Voce cadastrou {len(princ)}')
print(f'O maior peso foi de {maior}kgs. Peso de', end=' ')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi de {menor}kgs. Peso de', end=' ')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
print()
