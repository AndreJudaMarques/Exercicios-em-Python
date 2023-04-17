print()
    
numeros = []

valor = int(input('Digite o 1º valor: '))
numeros.append(valor)
print('Adicionado ao final da lista...')

for i in range(1,5):
    valor = int(input(f'Digite o {i+1}º valor: '))
    if valor > numeros[-1]:
        numeros.append(valor)
        print('Adicionado ao final da lista...')
    elif valor < numeros[0]:
        numeros.insert(0,valor)
        print('Adicionado na posição 0 da lista...')
    elif  numeros[0] < valor < numeros[1]:
        numeros.insert(1,valor)
        print('Adicionado na posição 1 da lista...')
    elif numeros[1] < valor < numeros[2]:
        numeros.insert(2,valor)
        print('Adicionado na posição 2 da lista...')
    elif valor > numeros[2]:
        numeros.insert(3,valor)
        print('Adicionado na posição 3 da lista...')
print('-=' * 15)
print(numeros)
print()
