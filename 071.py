'''cedulas de 50, 30, 10, 1'''
''' logica enquanto houver cedulas de 50
sacar as cedulas e retirar do total restante
o restante sera dividido por outras cedulas'''

'''cedulas de 50, 30, 10, 1'''
''' logica enquanto houver cedulas de 50
sacar as cedulas e retirar do total restante
o restante sera dividido por outras cedulas'''

titulo = 'BANCO PRO'
print('===' * 15)
print(f'\033[31m{titulo:^40}\33[m')
print('===' * 15)

valor = int(input('Que valor você quer sacar R$: '))

cont50 = 0
cont20 = 0
cont10 = 0
cont1 = 0

restante = 0

while restante + 50 <= valor:
    restante += 50
    cont50 += 1

while restante + 20 <= valor:
    restante += 20
    cont20 += 1

while restante + 10 <= valor:
    restante += 10
    cont10 += 1

while restante + 1 <= valor:
    restante += 1
    cont1 += 1

print(f'Total de {cont50} cédulas de R$50')
print(f'Total de {cont20} cédulas de R$20')
print(f'Total de {cont10} cédulas de R$10')
print(f'Total de {cont1} cédulas de R$1')
print()
sair = input('Pressione ENTER para sair... ')

