''' ler uma frase qualquer

-> quantas vezez aparece "A" 
-> em que posicao aparece 1 vez
-> em que posicao apaarece ultima vez'''

frase = input('Digite uma frase qualquer: ').upper().strip()

print(frase.count('A')) #maiusculo

print(frase.find('A')+ 1)

print(frase.rfind('A')+1)