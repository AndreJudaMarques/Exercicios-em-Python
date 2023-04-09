''' ler varios numeros,
parar quando digitar 999
mostrar soma entre eles
sem o flag(999)'''

print('A seguir vamos ler vários numeros ')

print('Digite um numero: ')
numero = int(input('--->: '))
print()

lista = []
lista.append(numero)

cont = 0

while numero != 999:
    print('Digite outro numero\nOu 999 para PARAR ')
    numero = int(input('--->: '))
    lista.append(numero)
    cont += 1
print()
lista.pop()
print(f'O resultado da soma dos {cont} números digitados é = {sum(lista)}')
print()


''' solucao video:
soma = cont = 0
while true:
    n = input(digite numero)
    if numero == 999:
        break
    cont +=1
    soma += numero
    
print(f'A soma dos {cont} valores foi {soma}')'''