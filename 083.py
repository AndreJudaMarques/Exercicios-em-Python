''' ler uma expressao qualquer
analisar se a expressao esta na ordem correta
'''
print()
exp = input('Digite uma expressão: ')
cont1 = 0
cont2 = 0

for letra in exp:
    if letra == "(":
        cont1 += 1
    if letra == ")":
        cont2 += 1
print()
if cont1 == cont2:
    print('Sua expressão é Válida! ')
else:
    print('Sua expressão está errada! ')
print()
