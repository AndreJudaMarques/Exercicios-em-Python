''' dicionarios '''
#dados = dict()

dados = { 'nome':'Pedro', 'idade':25 }
print(dados['idade'])

dados['sexo'] = 'M'

print(dados)

#del dados['idade'] elimina o elemento e valor

filmes = {
    'titulo':'Star Wars',
    'ano':1977,
    'diretor': 'George Lucas'
}
'''print(filmes.values()) # star wars, 1977, george
print(filmes.keys()) # titulo, ano, diretor
print(filmes.items()) # os 2 acima'''

'''for k, v in filmes.items():
    print(f'O {k} é {v}')'''

'''locadora = []
locadora.append(filmes)
print(locadora[0]['ano'])'''

pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':'22'}
del pessoas['sexo']
pessoas['peso'] = 98.5
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas)