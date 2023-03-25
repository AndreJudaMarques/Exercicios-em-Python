''' Aprovar credito bancario
comprar casa.
perguntar o valor da casa, valor do salario e em quantos anos quer pagar

calcular valor da prestacao mensal
nao pode exceder 30% do salario ou entao emprestimo negado'''

print('-=-' * 12)
print('Programa de Financiamento de Casa')
print('-=-' * 12)
print(' ')
print('Neste programa vamos verificar a possibilidade \n de você poder financiar um imóvel. ')
print(' ')
nome = input('Primeiramente digite seu nome: ')
print(' ')
valorDaCasa = float(input('Agora digite o valor da casa que você \n gostaria de comprar: R$ '))
print(' ')
salario = float(input('Qual o seu salário atualmente? R$ '))
print(' ')
anos = int(input('Em quantos anos gostaria de pagar esta casa? '))
print(' ')

quantidadeDeParcelas = anos * 12 #quantidade de parcelas

limiteDaParcela = (salario * 30) / 100

valorDaParcela = valorDaCasa / quantidadeDeParcelas

#o valor da casa / anos deve ser igual a 30% do salário 
#casa 200 mil
#salario 3mil (900 = 30%)
#pagar 30 anos = 30 * 12 = 360 vezes

if valorDaParcela < limiteDaParcela:
    print('Prezado sr.(a) {}, seu crédito foi aprovado e você poderá comprar a casa \n com as condições descritas.' .format(nome))
    print('Seu financiamento será de {} x de R${:.2f} '.format(quantidadeDeParcelas, valorDaParcela * 1000))
else:
    print('Infelizmente o financiamento não será aprovado \n pois o valor da parcela excede 30% do seu salário')
    print('Tente aumentar a quantidade de anos a pagar para reduzir o valor da parcela.')
print(' ')