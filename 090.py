dic = {}
n = input('Nome: ')
m = float(input('Média: '))
dic['nome'] = n
dic['média'] = m

#pode ser: dic['nome'] = input('Nome: ') já adiciona no dicionario

print(f'Nome é igual {dic["nome"]}')
print(f'Média é igual {dic["média"]}')

if m >= 7 :
    print('Situação é igual a Aprovado')
else:
    print('Situação é igual a Reprovado')
