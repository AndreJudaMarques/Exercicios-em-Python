
numero = int(input(' Digite um numero para tabuada: '))

tabuada = 1

print(' A tabuada do numero {} é: ' .format(numero))

while tabuada <= numero:
    numero * tabuada
    resultado = numero * tabuada
    print(' {} x {} = {}  ' .format(tabuada, numero, resultado) )
    tabuada +=1
print()


