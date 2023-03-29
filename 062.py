''' mostrar mais quantos termos'''

#EU QUE RESOLVI ESSA PORRA !!! 

termo = int(input('Digite o primeiro termo: '))

razao = int(input('Digite a razao: '))

cont = 1

while cont < 10:
    print(termo, end = ' ')
    while cont < 10:
        termo = termo + razao
        cont += 1
        print(termo, end=' ')
    print('\nVocê gostaria de ver mais termos?\n Digite quantos termos ou 0 para terminar. ')

escolha = int(input('--->: ')) #ex 2

if escolha == 0:
    print()
    quit

# cont chega com 10
# ex: escolha 2
else:
    #ex: escolha = 2
    escolha = cont - escolha #igual 8
    while escolha < cont: #ex 2 < 10
        termo = termo + razao #continua contagem do termo
        escolha = escolha + 1 #escolha esta meor que o cont dai para 
        print(termo, end=' ')
        #agora o problema esta na matematica
    print()
print()

    