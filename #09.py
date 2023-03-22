#Nessa aula, vamos aprender operações com String no Python.
# As principais operações que vamos aprender são o Fatiamento de String,
# Análise com len(), count(), find(), transformações com replace(), 
#upper(), lower(), capitalize(), title(), strip(), junção com join().

frase = 'Curso em Video Python'

print(frase[9]) #= V

print(frase[9:13])# =Vide

print(frase[9:21:2]) # saltando de 2 em 2

print(frase[15:])

print(frase[9::3])

print(len(frase))

print(frase.count('o'))

print(frase.count('o', 0, 13)) #entre o 0 e o 13 tem apenas 1 ó

print(frase.find('deo')) # começou na posicao 11, = 11

print(frase.find('Android')) # = -1 , significa que nao foi encontrado


print('Curso' in frase) # = True

print(frase.replace('Python', "Android")) # =Curso em Video Android( só no print, nao subistitui na variavel)

# upper e lower para maiuscula e minuscula

print(frase.upper())

print(frase.lower())

print(frase.capitalize()) # Só o primeiro char maiusculo

print(frase.title()) # cada palavra inicia com maiuscula

#strip() tira espaços inúteis
print(frase.strip())

#join() une as palavras

#split() divide os espaços, divide as palavras e refaz os indicies, formando lista para cadas palavras
print(frase.split())

print("""---> Nessa aula, vamos aprender operações com String no Python.
# As principais operações que vamos aprender são o Fatiamento de String,
# Análise com len(), count(), find(), transformações com replace(), 
#upper(), lower(), capitalize(), title(), strip(), junção com join().""")

#aspas 3x para imprimir o texto todo
