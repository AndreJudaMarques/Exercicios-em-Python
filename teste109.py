from ex109 import moeda

print()

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p, False)}')
print(f'O dobro de {p} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumento(p, False)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, True)}')

print()
