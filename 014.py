#conversor de temperaturas

temp = float(input('Informe a temperatura em ºC: '))

fahrenheit = (temp * 1.8) + 32

print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF! '.format(temp, fahrenheit))