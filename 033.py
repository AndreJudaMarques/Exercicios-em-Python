'''ler 3 numero 
mostrar qual maior e menor '''

numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))
numero3 = int(input('Digite mais um numero: '))


#verificando quem e menor

menor = numero1

if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3<numero2:
    menor = numero3
#verificando menor

maior = numero1

if numero2> numero1 and numero2> numero3:
    maior = numero2
if numero3>numero1 and numero3>numero2:
    maior = numero3

print('O menor valor digitado foi {}' .format(menor))
print('O maior valor digitado foi {} '.format(maior))