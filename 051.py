'''ler primeiro termo e a razao de uma progressao aritimetica, n
mostre 10 primeiros termos'''

termo = int(input('Digite o primeiro termo: '))

razao = int(input('Digite a razao: '))

decimo = termo + (10 - 1) * razao

for c in range(termo, decimo + razao, razao):
    c * 10
    print(c, end=' ')
