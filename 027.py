''' ler um nome completo, mostrar o primeiro e ultimo separadamente
primeiro: ana
ultimo: souza '''

nome = input(' Digite seu nome completo: ').strip()

n = nome.split()

print(n[0]) 
print(n[-1])
