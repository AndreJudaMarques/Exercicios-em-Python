''' ler 6 numeros inteiros mostra a soma dos pares'''

soma = 0

for c in range(0,6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
print(soma)