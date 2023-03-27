''' ler numero inteiro , se é primo ou nao '''

#solucao do video pq o exercicio e chato
#porem vou comentar tudo para aprender outra maneira de fazer

n = int(input('Digite um numero : ')) # le o numero

tot = 0 # verifica total de divisiveis

for c in range (1, n +1 ): #percorre entre o numero 1 e o numero digitado input
    if n % c == 0: #verifica se o numero é divisivel pelo contador
        print('\033[33m', end=' ') #printa o contador
        tot += 1 #verifica o total de contadores
    else:
        print('\033[31m', end=' ') #printa outro contador
    print('{} ' .format(c), end =' ')
print('\n\033[mO numero {} foi divisivel {} vezes ' .format(n, tot))
if tot == 2: #se for divisivel por 1 ou ele mesmo
    print('É primo! ')
else:
    print('Não é primo! ')
print()
