''' ler comprimento 3 retas
pode ou nao formar triangulo'''

print('-=-' * 20)
print('Analisador de Triangulos ')
print('-=-' * 20)

s1 = float(input('Digite o Primeiro seguimento: '))
s2 = float(input('Digite o Segundo seguimento: '))
s3 = float(input('Digite o Terceriro seguimento: '))

#cada seguimento tem que ser menor do que a soma do comprimento dos outros 2

if s1 < s2 + s2 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os seguimentos podem formar triangulo ')
else:
    print('Os seguimentos nao podem formar triangulo')