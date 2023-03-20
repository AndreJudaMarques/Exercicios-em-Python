largura = float(input(' Qual a largura da parede? '))
altura = float(input(' Qual a largura da parede? '))

area = largura * altura

#cada 1 litro = 2m²

tinta = area / 2

print(' A área da sua parede é de {}m² \n e será necessário {:.2f} litros de tinta para pintar' . format(area, tinta))