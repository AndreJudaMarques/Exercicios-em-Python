''' soma numeros multiplos de 3 entre 1 e 500'''

soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(soma, cont)