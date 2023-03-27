''' ler peso de 5 pessoas, qual foi maior peso
e qual menor peso'''

#minha solucao, queria ter feito diferente

print('Serão lidos pesos de 5 pessoas! ')

maior = 0
menor = 1000
for cont in range(1,6):
    peso = float(input('Digite o peso da {} pessoa: ' .format(cont)))
    if peso > maior:
        maior = peso
    elif peso < menor:
            menor = peso
            if peso < menor:
                menor = peso
print('O maior peso foi {}kg ' .format(maior))
print('O menor peso foi {}kg ' .format(menor))
print()

