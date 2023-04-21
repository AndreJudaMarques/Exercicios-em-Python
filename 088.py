'''ajude um jogar da mega sena a criar palpites

 programa pergunta quantos jogos serao gerados
 e vai sortear 6 numeros
 
 entre 1 e 60
 
 cadastrar tudo em uma lista composta'''

print()
print('---' * 15)
print('             JOGA NA MEGA SENA')
print('---' * 15)

import random

jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=-' * 2, f'SORTEANDO {jogos} JOGOS', '-=-' * 2)

for i in range(0, jogos):
    numero = random.sample(range(1,60), 6)
    print(f'Jogo {i+1}: {numero}')
  
print('-=-' *5, '< BOA SORTE! >', '-=-' *5)
print()
sair = input('Tecle ENTER para sair...')