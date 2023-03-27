''' refazer ex 9, tabuada com laço for '''

print('-=-' * 12 )
print('Programa de TABUADA')
print()

print('Digite o numero que gostaria de fazer a TABUADA')
numero  = int(input())
print()

for c in range(1, 11):
    print('{} x {} = {}' .format(c, numero, c * numero))
print()