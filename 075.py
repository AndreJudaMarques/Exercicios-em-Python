''' ler 4 valor 
guardar na tupla

a quantos 9

b posicao numero 3

c quais foram os pares'''

print()

numeros = []

contLoop = 0
cont9 = 0
contPar = []

while contLoop < 4:
    numero = int(input('Digite um número: '))
    if numero == 9:
        cont9 += 1
    if numero % 2 == 0:
        contPar.append(numero)
    numeros.append(numero)
    contLoop += 1

print()
print(f'Você digitou os valores: {numeros}')
print(f'-O valor 9 apareceu {cont9}')
if numero == 3:
    print(f'-O número 3 apareceu na {numeros.index(3)+1}º posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print(f'-Os valores pares digitados foram {contPar}')
print()