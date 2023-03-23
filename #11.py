'''Cores no terminal '''

''' ANSI
    
\033[STYLE;TEXT;BACKm '''

#print('\033[0;33;44m O')

'''STYLE
    0 none
    1 bold
    4 underline
    7 negative'''

''' text
    30 branco
    31 vermelhor
    32 verde
    33 amarelo 
    34 azul
    35 ciano
    36 magenta
    37 cinza padrao
    '''

'''back
    40 mesmas cores que o texto
    ...
    47'''
'''
print('\033[0;30;41m TESTE')

print('\033[4;33;44m TESTE')

print('\033[1;35;43m TESTE')

print('\033[30;42m TESTE')

print('\033[m TESTE')

print('\033[7;30m TESTE')

print('\033[m TESTE')

print('\033[31mOla Mundo\033[m')

print('\033[1;31;43mOla Mundo\033[m')'''

nome = input('Qual seu Nome: ')

cores = {'limpa' : '\033[m', #isso é um dicionario
         'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'pretoebranco' : '\033[7;30m'} #este nao esta funcioando, talvez terminal

print('Muito prazer em te conhecer {}{}{}! '.format(cores['pretoebranco'],nome, cores['limpa']))
