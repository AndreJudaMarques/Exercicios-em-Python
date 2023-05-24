
def voto():
    from datetime import date
    print('---' * 20)
    anoDeHoje = date.today().year
    anoInput = int(input('Em que ano você nasceu? '))
    idade = anoDeHoje - anoInput
    if 18 <= idade < 65:
        print(f'Com {idade} anos o VOTO é OBRIGATÓRIO')
    if idade >= 65:
        print(f'Com {idade} anos VOTO é OPCIONAL')
    if idade <18:
        print(f'Com {idade} anos NÃO pode VOTAR')
    print('---' * 20)
    print()

voto()
