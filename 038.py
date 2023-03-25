'''ler 2 numeros inteiros
comparar
valor maior e menor
ou iguais '''

print('-=-' * 12)
print(' Comparar valores: ')
print('-=-' * 12)

n1 = float(input('Digite um número: '))
n2 = float(input('Digite o segundo número: '))
print()

if n1 > n2:
    print("{} é o maior entre os dois ".format(n1))
elif n1 < n2:
    print("{} é o maior entre os dois ".format(n2))
else:
    print('Não existe maior, os valores são iguais ')

print()