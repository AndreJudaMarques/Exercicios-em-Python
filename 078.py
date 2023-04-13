'''ler 5 valores guardar numa lista
for com range

maior valor e menor valor digitado

e suas posicoes na lista'''
print()
valores = []

for v in range(0,5):
    valor = int(input(f'Digite um valor para a posição {v}: '))
    valores.append(valor)
print('=-=' * 15)
print(f'Você digitou os valors {valores}')
print(f'O maior valor digitado foi {max(valores)} na posição {valores.index(max(valores))}')
print(f'O menor valor digitado foi {min(valores)} na posição {valores.index(min(valores))}')
    
print()