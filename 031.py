'''distancia de uma viagem em km
calcular preço da passagem
50 centavos por km ate 200km
45 centavos para viagens mais longas'''

distancia = int(input('Digite a distância da sua viagem em km? '))

#50 centavos por km ate 200km

#45 centavos para viagens mais longas

preco1 = distancia * 0.50 # entao se 10km deve custar 5R$

preco2 = distancia * 0.45

if distancia < 200:
    print('O preço da sua passagem é de R${}. '.format(preco1))
else:
    print('O preço da sua passagem é de R${}. '.format(preco2))