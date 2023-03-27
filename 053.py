''' ler uma frase e se é palindromo'''

#solucao video, vou anotar tudo para aprender

frase = input('Digite uma frase: ').strip().upper() #remove todos os espacos e coloca tudo maiuscula

palavras = frase.split() #divide as palavras numa lista

junto = ''.join(palavras) #une as palavras sem espaço

inverso = '' # aqui recebe nada mas abaixo recebe a palavra invertido

for letra in range(len(junto) - 1, -1, -1): # le a palavra e inverte
    inverso += junto[letra] #recebe a palavra invertida
if inverso == junto: #verifica se inverso é igual junto
    print('Temos um palindromo! ')
else:
    print('A frase nao e um palindromo! ')

#print("Voce digitou a frase '{}'" .format(junto))