'''funcao contador 3 parametros inicio, fim, passo'''
from time import sleep
''' i= inicio f= fim p=passo '''
def linha():
    print('-=-' * 10)

def contagem(i, f, p):
    linha()
    print(f'Contagem de {i} até {f} de {p} em {p}')
    while p <= f:
        print(p, end=' ')
        #sleep(0.5)
        p += 1
    print('FIM!')

def contagem2(i, f, p):
    linha()
    print(f'Contagem de {i} até {f} de {p} em {p}')
    while i >= f:
        print(i, end=' ')
        i = i - p
    print('FIM!')

def contagem3(inicio, fim, passo):
    linha()
    print('Agora é sua vez de personalzar a contagem! ')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if passo < 0:
         linha()
         print(f'Contagem de {inicio} até {fim} de 1 em 1')
         while inicio >= fim:
              print(inicio, end=' ')
              inicio = inicio + passo # - com + da menos
    
    elif passo == 0:
        linha()
        print(f'Contagem de {inicio} até {fim} de 1 em 1')
        if inicio > fim:
            while inicio >= fim:
                print(inicio, end=' ')
                inicio -= 1
        else:
            while inicio <= passo:
                print(inicio, end=' ')
                inicio += 1

    else:    
        if inicio < fim:
                linha()
                print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
                while inicio <= fim:
                    print(inicio, end=' ')
                    inicio = inicio + passo
        elif inicio > fim and passo > 0:
            linha()
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
            while inicio >=fim:
                print(inicio, end=' ')
                inicio = inicio - passo
    
              
    print('FIM! ')

contagem(1,10,1)
contagem2(10,0,2)
contagem3(inicio=input, fim=input, passo=input)
print()