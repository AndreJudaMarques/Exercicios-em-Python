def sistemaDeAjuda():
    from time import sleep
    titulo = " Sistema de Ajuda PyHelp "
    cor_fundo_amarelo = "\033[48;2;255;255;0m"
    cor_fundo_azul = "\033[48;2;0;0;255m"
    cor_fundo_branco = "\033[48;2;255;255;255m"
    cor_fundo_rosa = "\033[48;2;255;105;180m"
    resetar_formato = "\033[0m"
    tamanho = len(titulo) + 4 # 2 tios para cada lado
    while True:
        print('~' * tamanho)
        print(f'  {cor_fundo_amarelo}{titulo}{resetar_formato}')
        print('~' * tamanho)
        #print(f"")
        comando = input('Função ou Biblioteca > ')
        if comando == 'fim':
            print(f'{cor_fundo_rosa}ATÉ LOGO!{resetar_formato}')
            print()
            break
        else:
            acessando = f"Acessando o manual do comando '{comando}'"
            #print(f" Acessando o manual do comando '{comando}'")
            tamanho2 = len(acessando) + 4
            print('~' * tamanho2)
            print(f"  {cor_fundo_azul}{acessando}{resetar_formato}")
            print('~' * tamanho2)
            sleep(2)
            print(f'{cor_fundo_branco} {help(comando)} {resetar_formato}')
            print(f"")
        
sistemaDeAjuda()


#help(print)