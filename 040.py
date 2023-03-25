'''ler 2 notas 
calcular media

abaixo de 5 reprovado
5 e 6.9 recuperacao

7.0 aprovado
'''

print('_=_' * 11)
print('Programa para verificar média para aprovação')
print('_=_' * 11)

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media < 5.0:
    print('O aluno está REPROVADO! ')

elif media >= 5.0 and media < 7:
    print('O aluno está de RECUPERAÇÃO')

else:
    print('O aluno está APROVADO! ')