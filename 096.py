print()
print('Controle de terrenos')
print('---' * 8)

largura = float(input('Largura: (m) '))
comprimento = float(input('Comprimento: (m) '))

def area():
    area = largura * comprimento
    print(f'A área do seu terreno de {largura}x{comprimento} é de {area}m²')
    print()

area(  )