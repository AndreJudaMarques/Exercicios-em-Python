'''calcular valor de um produto, considerando preço normal e 
condicoes de pagamento

a vista dinheiro ou cheque 10% desconto

a vista no cartao
5% de desconto

2x no cartao
sem juros

3x ou mais
20% juros'''

print('_-_' * 11)
print('Programa verifica condições de pagamento')
print('_-_' * 11)

valorDoProduto = float(input('Digite o valor do produto: R$ '))

print('Digite:\n 1-)para Pagamento à vista ou cheque.\n 2-) para Pagamento à vista no cartão.\n 3-) para Pagamento 2x no cartão.\n 4-)para Pagamento 3x ou mais')
condicao = int(input())
print()

descontoDeDEZ = (valorDoProduto * 10) / 100
descontodeCINTO = (valorDoProduto * 5) / 100
jurosDeVinte = (valorDoProduto * 20) / 100

if condicao == 1:
    valorDoProduto = valorDoProduto - descontoDeDEZ
    print('O valor do produto será de R${:.2f}\n Considerando 10% de desconto'.format(valorDoProduto * 1000))

elif condicao == 2:
    valorDoProduto = valorDoProduto - descontodeCINTO
    print('O valor do produto será de R${}\n Considerando 5% de desconto'.format(valorDoProduto * 1000))

elif condicao == 3:
    print('O valor do produto pode ser parcelado em até 2x de R${:.2f}\n parcelamento sem juros. '.format((valorDoProduto / 2) * 1000))

elif condicao == 4:
    valorDoProduto = valorDoProduto + jurosDeVinte
    print('O valor do produto será de R${:.2f}\n Considerando os juros de parcelamento'.format(valorDoProduto * 1000))

else:
    print('Número de Opção inválido! Tente novamente.')
print()