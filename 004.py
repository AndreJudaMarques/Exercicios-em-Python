char = input('Digite qualquer coisa: ')

print('O tipo primitivo disso é: ', type(char))
print('Só tem espaços? ', char.isspace())
print('É um número? ', char.isnumeric())
print('É composto de letras? ', char.isalpha())
print('Está em maiuscula? ', char.isupper())
print('Está em minuscula? ', char.islower())
print('Está capitalizada? ', char.istitle())