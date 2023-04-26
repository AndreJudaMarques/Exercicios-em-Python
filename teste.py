'''lista = [['andre', 1.0, 2.0], ['maria', 3.0, 4.0]]

print(lista[1][1:3])
'''


valor = int(input(' preço : '))
qtd = int(input('quantidade: '))

total = valor * qtd

if qtd >= 25 or valor > 200:
    desconto = 0.08 * total
    total -= desconto

print(f'valor final: {total} ')