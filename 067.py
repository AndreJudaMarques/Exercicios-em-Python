''' rodar programa tabuada enquanto for positivo'''
print('***O programa PARA quando valor for NEGATIVO***')
print('-' * 10)
tabuada = int(input('Quer ver a tabuada de qual valor? '))
print('-' * 10)

cont = 0

''' 
1 x tabuada = 
2 x tabuada = '''

while tabuada >= 0: #ex: 5
    while cont < 10:
        cont += 1
        print(f'{tabuada} x {cont} = {tabuada * cont}')
            
    print('-' * 10)
    tabuada = int(input('Quer ver a tabuada de qual valor? '))  
    cont = 0

print('-' * 10)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
print('-' * 10)
