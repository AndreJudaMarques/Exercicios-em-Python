'''TUPLAS SAO IMUTAVEIS
() tupla
[] listas
{} dicionario

'''
#tupla com ou sem ()
#TUPLAS SAO IMUTAVEIS
lanche = ('hamburguer', 'suco', 'pizza', 'puzim')
print(lanche)

'''for c in lanche:
    print(f'Eu vou comer {c}')
print('comi muito')
print(len(lanche))'''

for cont in range(0, len(lanche)):
    print(lanche[cont])

#pode apagar tupla
#del(lanche)
#print(lanche)
