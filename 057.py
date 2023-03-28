''' ler se é M ou F , se estiver errado novamente'''

print("Digite seu sexo ('M') ou ('F') ")

sexo = input().upper()


while sexo != 'M' or sexo != 'F':
    print('Inválido')
    sexo = input('Digite o sexo novamente M ou F: ').upper()
    if sexo == 'M':
        print('É masculino! ')
        break
    elif sexo == 'F':
        print('É feminino! ')
        break

    ''' enquanto o valor digitado for diferente de M ou F
    pergunta sexo de novo'''