'''ler ano nascimento de atleta
mostrar categoria'''

from datetime import date

anoNascimento = int(input('Digite o ano de nascimento do atleta: '))
print()

anoAtual = date.today().year #'''ANO ATUAL'''

idade = anoAtual - anoNascimento


if idade <=9:
    print('A categoria do atleta é: MIRIM! ')
elif idade > 9 and idade <= 14:
    print('A categoria do atleta é: INFANTIL! ') 
elif idade <= 19:
    print('A categoria do atleta é: JUNIOR! ')
elif idade <=20:
    print('A categoria do atleta é: SêNIOR! ')
else:
    print('A categoria do atleta é: MASTER! ')
print()