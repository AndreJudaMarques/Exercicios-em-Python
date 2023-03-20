#progama que leia um angulo qualquer e mostra o valor de seno, cosseno e tangente

import math

ang = float(input('Qual o valor do angulo? '))

''' math.sin
    math.cos
    math.tan '''

# math.radians(ang) tem que converter o angulo em radiano

seno= math.sin(math.radians(ang)) #o python faz o canculo do seno, ( math.radians converteu o ang em radianos)
cosseno= math.cos(math.radians(ang))
tangente= math.tan(math.radians(ang))

print(' O seno do angulo {} é {:.2f}  \n O Cosseno de {} é {:.2f} \n E o tangente de {} é {:.2f} ' .format(ang, seno, ang, cosseno, ang, tangente))
