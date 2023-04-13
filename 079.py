''' digitar varios valores numericos

cadatrar numa lista

caso ja exista na lista nao sera adicionado

no final todos os valores unicos exibidos em ordem crescente'''

print()

lista = []

while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
    else:
        print('Valor duplicado! Não vou adicionar')
    continuar = input('Quer continuar? [S/N]: ').upper()
    if continuar == 'N':
        break

print(sorted(lista))

print()

