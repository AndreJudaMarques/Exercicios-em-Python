''' pedir um numero, e mostrar a quantidade de numero da sequencia fibonacci'''


# F(n + 2) = F(n + 1) + F(n)
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, ...

''' fibonacci = 
f1 = 1
f2 = 1
f1  f2  resultado
1 + 1 = 2           | f1 + f1 = resultado // 1 + 1 = 2
2 + 1 = 3           | f2 = resultado + f1
3 + 2 = 5           | resultado = resultado + f2
5 + 3 = 8           | resultado + f2 = resultado'''

numero = int(input("Digite um numero: "))

cont = 1

f1 = 1
f2 = 1

resultado = 0

while cont < numero:
    print(f1,f2, end=' ') #saindo:  1
    while cont < numero:        
        cont += 1
        resultado = f1 + f2 #=2
        f2 = f1 #1
        f1 = resultado #=2        
        print(resultado, end=' ')


print('\n')
input('Digite qualquer coisa para sair...')
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, ...
