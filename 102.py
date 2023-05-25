def fatorial(n=0, show = False):
   print('---' * 15)
   if n == 0 or n == 1:
      resultado = 1
   else:
      antecessor = n - 1
      resultado = antecessor * n
      while antecessor > 1:
         if show == True:
            print(antecessor, end=' ')
         antecessor -= 1
         resultado = antecessor * resultado
   print(resultado)
   print('---' * 15)
   print()

fatorial(5, show=True)
   


