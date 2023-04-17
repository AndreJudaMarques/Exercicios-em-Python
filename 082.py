''' ler varios numeros e colocar numa lista

fazer uma lista so de pares e so de impares

no final mostrar 3 listas'''

print()

listaGeral = []
listaPar = []
listaImpar = []

while True:
    numero = int(input('Digite um número: '))
    listaGeral.append(numero)
    continuar = input('Quer continuar? [S/N] : ').upper()
    if continuar == 'N':
        break

for num in listaGeral:
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)

print()
print(f'Lista com todos valores {listaGeral}')
print(f'Os pares da lista {listaPar}')
print(f'Os ímpares da lista {listaImpar}')
print()