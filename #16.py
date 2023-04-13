'''listas sao mutaveis
tuplas nao 

append adiciona no final

insert adiciona na posicao
lanche.insert(0, 'hotdog')

del lanche[3] deleta

lanche.pop(3) pop deleta o ultimo

lanche.remove('pizza') indica o valor que quer eliminar
elimina o conteudo

if pizza in lanche:
    lanche.remove('pizza')

valores = list(range(4,11)) valores = lista de [4 ate 10]  exemplo(4,11,2) 4 ate 10 pulando de 2 em 2
valores.sort() em ordem
valores.sort(reverse=True) ordem inversa
len(valores)

---------

parte pratica
criar lista pode ser 2 maneiras

valores = [] 
ou 
valores = list()

'''

'''valores = []
#valores.append(5)
#valores.append(9)
#valores.append(4)

for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posicao {c} achei o valor {v}')
print('final')'''

a = [2, 3, 5, 7]
b = a # assim cria uma ligacao, muda um muda o outro || b = a[:] assim cria uma copia sem ligacao
b[2] = 8
print(f'Lista A {a}')
print(f'Lista B {b}')