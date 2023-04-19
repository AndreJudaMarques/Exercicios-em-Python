''' ler 7 valores numeros
cadastrar em lista unica
separar pares e impares em outras listas dentro dessa unica lista'''

numeros = []
pares = []
impares = []

print()
for i in range(0,7):
    valor = int(input(f'Digite o {i+1}º valor: '))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

numeros.append(pares)
numeros.append(impares)

print()
numeros.sort()
pares.sort()
impares.sort()
print(numeros)
print(f'Os valores pares digitados foram {pares}')
print(f'Os valores ímpares digitados foram {impares}')