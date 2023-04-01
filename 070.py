''' registrar varios produtos 
nome e preço
continuar s ou n 
print: 
    total da compra
    quantos produtos mais de 1.000
    nome do mais barato'''

titulo = 'LOJA SUPER BARATÃO'
print(' === ' * 10)
print(f'\033[34m{titulo:^50}\33[m')
print(' === ' * 10)

produto = input('Nome do produto: ')
#preco = float(input('Preço: '))

caro = 0

while True:
    try:
        preco = float(input('Preço: '))
        break
    except ValueError:
        print('Inválido, tente novamente...')

if preco > 1000:
    caro += 1

baratopreco = []
baratopreco.append(preco)

continuar = input('Quer continuar? [S/N] : ').upper()

total = preco

precoAnterior = preco

produtoMaisBarato = produto

while continuar == 'S':
    produto = input('Nome do produto: ')
    while True:
        try:
            preco = float(input('Preço: '))
            break
        except ValueError:
            print('Inválido, tente novamente...')

    if preco < precoAnterior:
        produtoMaisBarato = produto

    if preco > 1000:
        caro += 1
    total = total + preco
    baratopreco.append(preco) # salva todos preços na lista, no print joga o menor
    
    continuar = input('Quer continuar? [S/N] : ').upper()

print()
print('===== FIM DO PROGRAMA =====')
print(f'-O total da compra foi {total:.2f}\n-Temos {caro} produtos custando mais de R$1000.00\n-O produto mais barato foi {produtoMaisBarato} que custa R${min(baratopreco)}')
print()

sair = input('Digite qualquer coisa para sair... ')

'''' se preco < preco anterior 
baratoProduto = produto'''
