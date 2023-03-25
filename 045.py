''' criar um jokenpo com o computador'''

import emoji

from random import randint

print('_-_' * 12)
print('Programa do Jogo JOKENPÔ! ')
print(emoji.emojize(':raised_fist: :raised_hand: :victory_hand: '))
print()

print(emoji.emojize('É você contra o computador, BOA SORTE! :winking_face:'))
print()

pc = randint(1,3)

print(emoji.emojize('Digite: \n 1 para Pedra :raised_fist: \n 2 para Papel :raised_hand: \n 3 para Tesoura :victory_hand:'))
player = int(input())
print()

#player emojis
if player == 1:
    playerEmoji = emoji.emojize(':raised_fist:')
    print(player, playerEmoji)
elif player == 2:
    playerEmoji = emoji.emojize(':raised_hand:')
    print(player, playerEmoji)
elif player == 3:
    playerEmoji = emoji.emojize(':victory_hand:')
    print(player, playerEmoji)

#pc emojis
if pc == 1:
    pcEmoji = emoji.emojize(':raised_fist:')
    print(pc, pcEmoji)
elif pc == 2:
    pcEmoji = emoji.emojize(':raised_hand:')
    print(pc, pcEmoji)
elif pc == 3:
    pcEmoji = emoji.emojize(':victory_hand:')
    print(pc, pcEmoji)


#quem ganhou

if player  == pc:
    print('EMPATE! Você e o PC escolheram o mesmo, tente de novo. ')

if player == 1 and pc == 3:
    print('Você ganhou! pois PEDRA Quebra TESOURA. ')
elif player == 1 and pc == 2:
    print('Você Perdeu! pois PAPEL embrulha PEDRA. ')
elif player ==2 and pc == 1:
    print('Você ganhou! pois PAPEL embrulha PEDRA. ')
elif player ==2 and pc == 3:
    print('Você perdeu! pois TESOURA corta PAPEL. ')
elif player == 3 and pc == 1:
    print('Você perdeu! pois PEDRA Quebra TESOURA. ')
elif player == 3 and pc == 2:
    print('Você ganhou! pois TESOURA corta PAPEL. ')
print()

