''' digite 1 para somar
2 multiplicar
3 maior
4 novos numeros
5 sair do programa'''

from time import sleep

print('-*-' * 10)
print('Programa de 2 numeros')
print()

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
print()

print('''Digite: \n 1-) para SOMAR \n 2-) para MULTIPLICAR \n 3-) para MAIOR \n 4-) Novos Números \n 5-) SAIR do programa ''')

e = int(input('--->: '))

condicao = True

while condicao:
    if e == 1:
        print()
        print('A soma do {} + {} = {} ' .format(n1, n2, n1+n2))
        print()
        #sleep(1)
        break
        #sair = input('Digite qualquer coisa para sair...')
         
    elif e == 2:
        print()
        print('A multiplicação do {} x {} = {} ' .format(n1, n2, n1*n2))
        print()
        break

    elif e == 3:
        if n1 > n2:
            print('O maior número é o {} ' .format(n1))
        else:
            print('O maior número é o {} ' .format(n2))
        print()
        break

    elif e == 4:
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
        print()
        print('''Digite: \n 1-) para SOMAR \n 2-) para MULTIPLICAR \n 3-) para MAIOR \n 4-) Novos Números \n 5-) SAIR do programa ''')
        print()
        e = int(input('--->: '))

    elif e == 5:
        condicao = False
        #quit
    
    #elif e == '':
     #   print('Opção inválida, tente novamente ')

    else:
        print('Opção inválida, tente novamente ') 
        print()
        print('Seus numeros são {} e {} ' .format(n1, n2))
        print('''Digite: \n 1-) para SOMAR \n 2-) para MULTIPLICAR \n 3-) para MAIOR \n 4-) Novos Números \n 5-) SAIR do programa ''')
        e = int(input())
   

print()

'''sleep(2)
        print('Gostaria de ir de novo? S ou N')
        gostaria = input().upper()
        if gostaria == 'S':
            n1 = int(input('Digite o primeiro numero: '))
            n2 = int(input('Digite o segundo numero: '))
            print('Digite: \n 1-) para SOMAR \n 2-) para MULTIPLICAR \n 3-) para MAIOR \n 4-) Novos Números \n 5-) SAIR do programa ')
            e = int(input())
        elif gostaria =='N':
            quit'''