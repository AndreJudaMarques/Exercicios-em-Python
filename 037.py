''' bases numero
converter numero em base de conversao

input = int

conversao

1 binario
2 octal
3 hexadecimal'''

#solucao do video

num = int(input('Digite um numero inteiro '))

print('''Escolha uma opcao \n 1 binario \n 2 octal \n 3 hexadecimal''')

opcao = int(input())

if opcao == 1:
    print('{} convertido para binario = a {} ' .format(num, bin(num)))

elif opcao == 2:
    print('{} convertido para octal = a {} ' .format(num, oct(num)))

elif opcao == 3:
    print('{} convertido para hexa = a {} ' .format(num, hex(num)))

else:
    print(' opcao invalida, tente novamente ')

