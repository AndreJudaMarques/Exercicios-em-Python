dicionarios = {}

nomes = []

sexos = []

mulheres = []

idades = []

idadesCont = 0

while True:
    nome = input('Nome: ')
    nomes.append(nome)
    sexo = input('Sexo: [M/F] ')
    sexos.append(sexo)
    if sexo in 'fF':
        mulheres.append(nome)
    idade = int(input('idade: '))
    idades.append(idade)
    idadesCont = idadesCont + idade
    continuar = input('Quer continuar? [S/N] ')
    if continuar in 'nN':
        break

print('-=-' * 10)
#print(nome)

dicionarios['nomes'] = nomes
dicionarios['sexo'] = sexos
dicionarios['idade'] = idades

print(dicionarios) #deletar esta linha
print(f'O grupo tem {len(nomes)} pessoas')
print(f'A média de idade é de {idadesCont / len(nomes)}')
print(f'As mulheres cadastradas foram: {mulheres}')
print(f'Lista das pessoas acima da média: ')

for i, idade in enumerate(idades):
    if idade > idadesCont / len(nomes): #chatGPT me ajudou a relacionar o enumerate com outras listas
        print(f'nome = {nomes[i]}; sexo = {sexos[i]}; idade = {idade}')
print('<< ENCERRADO >>')
print()