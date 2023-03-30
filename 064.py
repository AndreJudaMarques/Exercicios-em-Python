''' ler varios numeros,
parar quando digitar 999
mostrar quantos foram digitados
e a soma entre eles
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
print('Os números digitados foram:\n',lista, '\nForam digitados {} números ' .format(cont), '\nO resultado da soma dos números digitados é = {} '.format(sum(lista)))
print()




