from ex107 import moeda

print()

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumento(p)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p)}')

print()
