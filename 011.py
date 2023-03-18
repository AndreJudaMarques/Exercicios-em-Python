largura = int(input(' Qual a largura da parede? '))
altura = int(input(' Qual a largura da parede? '))

area = largura * altura

#cada 1 litro = 2m²

tinta = area / 2

print(' A área da sua parede é de {}m² e será necessário {} litros de tinta para pint' . format(area, tinta))