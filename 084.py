'''cadastrar pessoas com nome e peso
dizer quntas tem na lista
os maiores pesos 100 kgs
os menores pesos 70 kgs'''


pessoas = list()

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
    print(f'{pessoa[0]}', end=' ')
