#progama ler o comprimento do cateto oposto e adjacente de um triangulo retangulo
# calcule e mostre o comprimento da hipotenusa

import math

catetoOposto = float(input(' Qual comprimento do cateto oposto? '))
catetoAdjacente = float(input(' Qual comprimento do cateto adjacente? '))

#hipotenusa = sqrt(cateto_oposto² + cateto_adjacente²)

hipotenusa = math.hypot(catetoOposto, catetoAdjacente)

print('O comprimento da Hipotenusa é {:.2f} '. format(hipotenusa))



