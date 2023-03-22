''' ler um nome completo
-> print todas maiusculas
-> todas minusculas
-> quantas letras sem considerar espacos
-> quantas letras primeiro nome'''

nome = str(input('Digite seu nome completo: '))

print(nome.upper()) #ok

print(nome.lower()) #ok

print(len(nome)-nome.count(' ')) #solucao pelo video 

print(len(nome.split()[0])) #ok

#Joao   da    Silva
#0123 4 56 7  89101112 = 13 + 0

#André    Judá
#01234  5 6789 = 10