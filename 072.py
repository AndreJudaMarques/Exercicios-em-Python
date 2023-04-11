'''escrever numero por extenso'''

print()
numeros = ('zero' , 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 
           'doze', 'treze', 'quartorze', 'quinze', 'desseseis', 
           'dessesete', 'dezoito', 'dezenove', 'vinte')

#minha solucao abaixo
'''numero = int(input('Digite um numero entre 0 e 20: '))

while  numero < 0 or numero > 20:
    numero = int(input('Tente novamente. Digite um numero entre 0 e 20: '))    

print(f'Voce digitou o numero {(numeros[numero])}')
print()'''

#solucao video abaixo

while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente. ', end=' ') 

print(f'Voce digitou o numero {(numeros[numero])}')    
print()