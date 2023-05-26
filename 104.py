def leiaInt():
     while True:
          try:
               numero = int(input('Digite um numero: '))
               break
          except ValueError:
               print('ERRO! Digite um número: ')
     print(f'Voce digitou o numero {numero}')

leiaInt()

#chat gpt help 