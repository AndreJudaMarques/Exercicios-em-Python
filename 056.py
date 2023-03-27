''' ler nome , idade e sexo de 4 pessoas

mostrar a media de idade do grupo
nome do homem mais velho
mulheres menos de 21 anos
'''
#MINHA SOLUCAO PARA ESTE EXERCICIO

print()
print('Vamos ler o nome , idade e sexo de 4 pessoas. ')
print('-=-' * 10)
print()
somaIdade = 0

idadeMaisVelho = 0

nomeMaisVelho = ''

mulheresMenores = []
contMenores = 0

for i in range(1,5):
    nome = input("Digite o nome da {}º pessoa: " .format(i))
    idade = int(input("Digite a idade da {}º pessoa: " .format(i)))
    sexo = input("Digite o sexo da {}º pessoa:('M') ou ('F') " .format(i)).upper()
    print('-' * 10)
    somaIdade = somaIdade + idade
    if sexo == 'M' and idade > idadeMaisVelho:
        idadeMaisVelho = idade
        nomeMaisVelho = nome
    elif sexo == 'F' and idade < 21:
        mulheresMenores.append(nome)
        contMenores += 1
mediaIdade = somaIdade / 4

print('A idade média do grupo é: {:.1f} ' .format(mediaIdade))
print('O home mais velho é o {} que possui {} anos. ' .format(nomeMaisVelho, idadeMaisVelho))
print('Existem {} mulheres menores que 21 e seus nome são {} ' .format(contMenores, mulheresMenores))
print()
