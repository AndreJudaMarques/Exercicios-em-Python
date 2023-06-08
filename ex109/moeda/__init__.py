
def dobro(x, cond = False):
    d = x + x
    if cond == True:
      return (f'R${d:.2f}')
    else:
      return d

def metade(x, cond = False):
    m = x / 2
    if cond == True:
      return (f'R${m:.2f}')
    else:
      return m

def aumento(x, cond= False):
    dez = x * 0.1
    aumento = x + dez
    if cond == True:
      return (f'R${aumento:.2f}')
    else:
       return aumento

def diminuir(x, cond=False):
    treze = x * 0.13
    reduzir = x - treze
    if cond == True:
      return (f'R${reduzir:.2f}')
    else:
       return reduzir