'''contagem regressiva de fogos de artificio 
contagem 10, pausa 1 sec'''

from time import sleep

import emoji

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize(':sparkles: :fireworks: :sparkles:'))