
def leiaDinheiro(x):
      import re
      valor = input(x)

      # Remove espaços em branco e símbolos monetários
      valor = re.sub(r'\s|[$]', '', valor)

      # Substitui a vírgula por ponto
      valor = valor.replace(',', '.')

      # Verifica se o valor é válido
      if re.match(r'^\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})?$', valor):
            #print("O valor monetário é válido:", valor)
            return float(valor)
      else:
            print("\033[91mERRO:\033[0m", valor, "é um preço inválido!")
            return None
