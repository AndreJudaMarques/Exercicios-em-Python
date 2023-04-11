'''tupla varias palavras

mostrar cada vogais das palavras'''

palavras = ('aprender', 'programar', 'linguagem',
             'python', 'curso', 'gratis', 'estudar',
               'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

print()

for palavra in palavras:
    vogais = []
    for letra in palavra:
        if letra in 'aeiou':
            vogais.append(letra)
    if vogais:
        print(f'Na palavra {palavra} temos as vogais {", " .join(vogais)}')
        
print()