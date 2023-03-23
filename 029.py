# ler velocidade do carro

#acima de 80 sera multado

#multa 7 por km acima

velocidade = int(input('Qual a velocidade do carro? '))

limite = 80

multa = (velocidade - limite) * 7

if velocidade > limite:
    print('Você foi multado pois estava acima da velocidade \n e o valor da sua multa será de R${}' .format(multa))
else:
    print('Você está dentro do limite! Parabéns.')