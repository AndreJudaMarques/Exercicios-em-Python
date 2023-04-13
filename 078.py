'''ler 5 valores guardar numa lista
for com range

maior valor e menor valor digitado

e suas posicoes na lista'''
print()
valores = []
#minhha solucao abaixo
'''for v in range(0,5):
    valor = int(input(f'Digite um valor para a posição {v}: '))
    valores.append(valor)
print('=-=' * 15)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições {valores.index(max(valores))}')
print(f'O menor valor digitado foi {min(valores)} nas posições {valores.index(min(valores))}')''' #minha solucao nao encontrei posicoes para maiores

#solucao video abaixo
mai = 0
men = 0
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c ==0:
        mai = men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c] 
        if valores[c] < men:
            men = valores[c]
print('=-=' * 15)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {mai} nas posições', end=' ')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}...', end='')
    
print(f'\nO menor valor digitado foi {men} nas posições', end=' ')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}...', end='')

print()
print()

