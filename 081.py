'''ler varios numeros
continuar sim ou nao
quantos numeros foram digitados
lista em forma decrescente

se 5 foi digitado e esta ou nao na lista
'''

print()

numeros = []

while True:
    valor = int(input('Digite um valor: '))
    numeros.append(valor)
    continuar = input('Quer continuar? [S/N] ').upper()
    if continuar == "N":
        break
print()
print(f'Você digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)#### tem que fazer o reverse antes de imprimir
print(f'Os valores em ordem decrescente são {numeros}' )
if 5 in numeros:
    print('O valor 5 faz parte da lista! ')
else:
    print('O 5 não está na lista')
print()
