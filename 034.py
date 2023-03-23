'''Pergunta salario e da aumento
superior  1250 aumento 10% 
inferior 15% '''

salario = float(input('Qual é o seu salário? '))

if salario > 1250:
    salario = salario * 1.10
    print('Seu novo salário com 10% de aumento é R${} '.format(salario))
else:
    salario = salario * 1.15
    print('Seu novo salário com 15% de aumento é R${} '.format(salario))