from random import randint

vezes = int(input('Quantas vezes quer executar o programa "Função Max"? '))

def maior():    
    print('-=-' * 10)
    print('Analisando os valores passados...')
    randNUM = randint(0,15)
    listaNumeros = []
    cont = 0
    while cont < randNUM:
        randNUM = randint(1,6)
        listaNumeros.append(randNUM)
        cont +=1

    print(listaNumeros, f'Foram informados {len(listaNumeros)} ao todo.')
    if len(listaNumeros) < 1:
        print('Foram inforamdos 0 valores ao todo.')
        print('O maior valor informado foi 0.')
    else:
        print(f'O maior valor informado foi {max(listaNumeros)}.')

conti = 0
while conti < vezes:
    maior()
    conti += 1

print()