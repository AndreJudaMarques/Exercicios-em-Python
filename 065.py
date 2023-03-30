'''igual anterior, com media entre numeros
maior
e menor
se quer continuar ou nao'''

print('*+*' * 10)
print('Vamos ler vários números ')
print('Com S para continuar ou N para Parar ')
print()

print('Digite um número ')

numero = int(input('--->: '))

lista = []

lista.append(numero)

cont = 1

deseja = input('Deseja continuar? \nS para continuar N para parar: ').lower()

while deseja != 'n':
    print('Digite outro número ')
    numero = int(input('--->: '))
    lista.append(numero)
    deseja = input('Deseja continuar? \nS para continuar N para parar: ').lower()
    cont +=1 

media = (sum(lista)) / cont

maior = max(lista)

menor = min(lista)
print()
print('Os números digitados foram:', lista, '\nA média entre todos os números é = {:.1f}\nO maior número digitado foi o {}\nE o menor foi o {} ' .format(media, maior, menor))
print()
