''' ler idade de sexo de varios
quer continuar

quantas mais de 18
quantos homens
quantas mulheres menos que 20'''

titulo = 'CADASTRE UMA PESSOA'
print('=--=' * 10)
print(f'\033[34m{titulo:^35}\033[m')
print('=--=' * 10)
#print('  ' * 10)

contIdade = 0
contH = 0
contM = 0

idade = int(input('Idade: '))

sexo  = str(input('Sexo: [M/F]: ')).upper()

while sexo != "M" and sexo != "F":
    sexo  = str(input('Sexo: [M/F]: ')).upper()

if idade > 18:
    contIdade += 1
if sexo == "M":
    contH += 1
if idade < 20:
    if sexo == "F":
        contM += 1

'''listaIdade = []
listaSexo = []
listaIdade.append(idade)
listaSexo.append(sexo)'''

print('=--=' * 10)
continuar = input('Quer continuar? [S/N]: ').upper()
print('=--=' * 10)

while continuar == "S":
    #print('=--=' * 10)  
    print(f'\033[34m{titulo:^35}\033[m')

    idade = int(input('Idade: '))
    sexo  = str(input('Sexo: [M/F]: ')).upper()
    while sexo != "M" and sexo != "F":
        sexo  = str(input('Sexo: [M/F]: ')).upper()
    if idade > 18:
        contIdade += 1
    if sexo == "M":
        contH += 1
    if idade < 20:
        if sexo == "F":
            contM += 1
    '''#listaIdade.append(idade)
    #listaSexo.append(sexo) ''' 
    print('=--=' * 10)
    continuar = input('Quer continuar? [S/N]').strip().upper()
    print('=--=' * 10)  


print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {contIdade} \nAo todo temos {contH} homens cadastrados \nE temos {contM} mulheres com menos de 20 anos')
print()
sair = input('Digite qualquer coisa para sair...')
