''' ler nome de pessoa e dizer se tem "SILVA" no nome '''

nome = input('Digite seu nome: ').strip()

'''if 'Silva' in nome:
    print('Tem Silva no nome')
else:
    print('Nao tem Silva no nome')'''

#abaixo solucao do video
print(' Seu nome tem Silva: {}' .format('SILVA' in nome.upper()))