'''criar matrix 3x3
linhas e colunas
mostrar na tela com formatacao correta
[[1] [2] [3] 
[4] [5] [6]
[7] [8] [9]]  

#matriz = [ [1], [2], [3]] 
matriz = []

linha1 = []
linha2 = []
linha3 = [] 

#matriz.append([2]) isso vale

#matriz.insert(1,[3]) isso vale

contlinha = 0
for i in range(0,1):
    for coluna in range(0,3): # linha 1
        n = int(input(f'Digite um valor para a posição [{contlinha}, {coluna}]: '))
        linha1.insert(coluna, [ n ])
    matriz.append(linha1)
    contlinha += 1

    for coluna in range(0,3): # linha 2
        n = int(input(f'Digite um valor para a posição [{contlinha}, {coluna}]: '))
        linha2.insert(coluna, [ n ])
    matriz.append(linha2)    
    contlinha += 1

    for coluna in range(0,3): # linha 3
        n = int(input(f'Digite um valor para a posição [{contlinha}, {coluna}]: '))
        linha3.insert(coluna, [ n ])
    matriz.append(linha3)
    contlinha += 1

cont= 0
for i in matriz:
    print(f'{matriz[cont]}')
    cont+= 1

    #explicação
    #fiz uma matriz com a linha 0 e coluna 0
      #coluna  
    #linha0  0  1  2
    #linha1  0  1  2
    #linha2  0  1  2'''

matriz = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]

for l in range(0, 3): #linha
    for c in range(0, 3): #coluna
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-=-' *15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='') #:^5  faz o print ficar centrlizado
    print()