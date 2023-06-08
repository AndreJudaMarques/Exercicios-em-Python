
def dobro(x):
    d = x + x
    return (f'R${d:.2f}')

def metade(x):
    m = x / 2
    return (f'R${m:.2f}')

def aumento(x):
    dez = x * 0.1
    aumento = x + dez
    return (f'R${aumento:.2f}')

def diminuir(x):
    treze = x * 0.13
    reduzir = x - treze
    return (f'R${reduzir:.2f}')