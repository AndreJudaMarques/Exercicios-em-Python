''' ler um numero entre 0 9999 e mostre cada digito separado
ex: 1832
-> unidade: 4
-> dezenas: 3
-> centena: 8
-> milhar: 1

fazer como string e matematicamente '''

numero = int(input(' Digite um numero entre 0 e 9999: '))

unidade = numero // 1 % 10

dezena = numero // 10 % 10

centena = numero // 100 % 10

milhar = numero // 1000 % 10

print('Unidade = {} ' .format(unidade))
print('dezena = {} ' .format(dezena))
print('centena = {} ' .format(centena))
print('milhar = {} ' .format(milhar))

#solucao pelo video

