# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = float(input(' Quantos dias alugado? '))
km = float(input(' Quantos km percorrido? '))

custoDoDia = dias * 60 #andou 8 dias = 8 * 60
custoDoKmRodado = km * 0.15 #rodou 720 km, cada km custou .15

custoTotal = custoDoDia + custoDoKmRodado

print(' O valor total a pagar é de R${:.2f} .' .format(custoTotal))

