texto = input('Digite o texto: ')

def mostraTexto():
    tamanho = len(texto) + 4 # 2 tios para cada lado
    print('~' * tamanho)
    print(f'  {texto:}')
    print('~' * tamanho)
    

mostraTexto()

print(len(texto))