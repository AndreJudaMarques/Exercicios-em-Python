''' ler nome de uma cidade
começa ou nao com nome "santo" '''

cidade = input('Digite o nome de uma cidade: ').strip()

print(cidade[:5].upper() == 'SANTO') #deu strip tirando espaços
#jogou tudo pra maiuscula e verificou a palavra

#solucao pelo video

