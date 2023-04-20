'''exercicio anterior com a soma dos pares
a soma dos valores da 3 coluna
e o maior da segunda linha'''

matriz = []

linha1 = []
linha2 = []
linha3 = [] 
pares = []
terceira = []
contlinha = 0
print()
print('Esta é a Matriz: \nLinha1 [0] [1] [2]\nLinha2 [0] [1] [2]\nLinha3 [0] [1] [2]')

for i in range(0,1):
    for coluna in range(0,3): # linha 1
        n = int(input(f'Digite um valor para a posição [{contlinha}, {coluna}]: '))
        linha1.insert(coluna, [ n ])
        if n % 2 == 0:
            pares.append(n)
        if coluna == 2:
            terceira.append(n)
    matriz.append(linha1)
    contlinha += 1

    for coluna in range(0,3): # linha 2
        n = int(input(f'Digite um valor para a posição [{contlinha}, {coluna}]: '))
        linha2.insert(coluna, [ n ])
        if n % 2 == 0:
            pares.append(n)
        if coluna == 2:
            terceira.append(n) 
    matriz.append(linha2)    
    contlinha += 1

    for coluna in range(0,3): # linha 3
        n = int(input(f'Digite um valor para a posição [{contlinha}, {coluna}]: '))
        linha3.insert(coluna, [ n ])
        if n % 2 == 0:
            pares.append(n)
        if coluna == 2:
            terceira.append(n)
    matriz.append(linha3)
    contlinha += 1

cont= 0
for i in matriz:
    print(f'{matriz[cont]}')
    cont+= 1
print(f'A soma dos valores pares é {sum(pares)}')
print(f'A terceira coluna é {terceira}')
print(f'A soma dos valores da terceira coluna é {sum(terceira)} ')
print(f'O maior valor da segunda linha é {max(linha2)}')
print()
sair = input('Aperte ENTER para sair...')