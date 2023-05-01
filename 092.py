dici = {

}

from datetime import datetime

noome = input('Digite o nome: ')
anonascimento = int(input('Ano de Nascimento: '))
ctps = int(input('Nº carteira de tralho (0 não tem): '))
dici['nome'] = noome
dici['nascimento'] = anonascimento
dici['carteira'] = ctps
if ctps != 0:
    anocontrato = int(input('Qual ano de contratação? '))
    salario = float(input('Qual era seu salário? '))
    dici['ano de contratação: '] = anocontrato
    dici['salário: '] = salario
print('-=-' * 10)
print(dici)

idade = datetime.today().year - anonascimento

print(f'Nome tem o valor {dici["nome"]}')
print(f'Idade tem o valor {idade}') 
if ctps != 0:
    print(f'ctps tem o valor {dici["carteira"]}')
    print(f'contratação tem o valor {dici["ano de contratação: "]}')
    print(f'salário tem o valor {dici["salário: "]}')
    contribuicao = datetime.today().year - anocontrato
    if contribuicao < 35:
       print(f'você ainda tem {35 - contribuicao} anos de contribuição')
    else:
        print(f'Você já pode se aposentar ')
#aposentadoria depois de 35 anos de colaboração
#ano de contratação + 35 anos
else:
    print(f'ctps tem o valor {dici["carteira"]}')
print()
