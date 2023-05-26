def notas(*n, situacao = False):
     print('---' * 15)
     diciNotas = {}
     diciNotas['Quantidade'] = len(n)
     diciNotas['Maior nota'] = max(n)
     diciNotas['Menor nota'] = min(n)
     media = sum(n) / len(n)
     diciNotas['Média'] = media
     if situacao:
          diciNotas['Classificação'] = 'BOA' if media > 5 else 'RUIM'
     '''for i, nota in enumerate(n): #aqui serve só para aparecer as notas
          diciNotas[f'Nota {i+1}'] = nota'''
     print(diciNotas)
     print()


notas(5, 6, 7, situacao=True)

