def resumo(x, y, z=0):
    porcentageAumento = y / 100 # = 0.8
    porcentagemReducao = z / 100 # = 0.35
    aumento = float(x) * porcentageAumento
    reducao = x * porcentagemReducao
    print('--' * 10)
    print(f'  RESUMO DO VALOR')
    print('--' * 10)
    print(f'Preço analisado:   R${x:.2f}')
    print(f'Dobro do preço:   R${2*x:.2f}')
    print(f'Metade do preço:   R${x/2:.2f}')
    print(f'{y}% de aumento:   R${x+aumento:.2f}')
    print(f'{z}% de redução:   R${x-reducao:.2f}')