
cont = 0

matriz = []
linha1 = []
#matriz.append([2]) isso vale

#matriz.insert(1,[3]) isso vale
print('Esta é a Matriz: \nLinha1 [0] [1] [2]\nLinha2 [0] [1] [2]\nLinha3 [0] [1] [2]')
for linha in range(0,1):
    for coluna in range(0,3): # linha 1
        n = int(input(f'Digite um valor para a posição {linha}, {coluna}: '))      
        linha1.append([n])
matriz.append(linha1)

print(matriz[0])

'''cont = 0
for i in matriz:
    print(matriz[cont], end=' ')
    cont += 1
'''
    