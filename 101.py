
def voto():
    from datetime import date
    print('---' * 20)
    anoDeHoje = date.today().year
    anoInput = int(input('Em que ano você nasceu? '))
    idade = anoDeHoje - anoInput
    if 18 <= idade < 65:
        print('VOTO OBRIGATÓRIO')
    if idade >= 65:
        print('VOTO OPCIONAL')
    if idade <18:
        print('NÃO VOTA')
    print('---' * 20)
    print()

voto()
