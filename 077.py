'''tupla varias palavras

mostrar cada vogais das palavras'''

palavras = ('aprender', 'programar', 'linguagem',
             'python', 'curso', 'gratis', 'estudar',
               'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

print()
#minha solucao com ajuda
'''for palavra in palavras:
    vogais = []
    for letra in palavra:
        if letra in 'aeiou':
            vogais.append(letra)
    if vogais:
        print(f'Na palavra {palavra} temos as vogais {", " .join(vogais)}')'''
        
#solucao do video 
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=', ')                 
print()
print()