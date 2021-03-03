# lib

def cabecalho(msg, c='sem'):
    linha()
    print(msg.center(40))
    linha()


def linha(n=40):
    print('-' * n)


def texto(msg, c='sem'):
    cor = {
        'sem': '\033[0;0m',
        'amarelo': '\033[0;33m',
        'azul': '\033[1;94m',
        'vermelho': '\033[1;31m',
        'branco': '\033[7;30m'
    }
    print(cor[c], end='')
    print(f'{msg}', end='')
    print(cor['sem'], end='')


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            texto('Erro! Por favor, digite um número inteiro válido.\n', 'vermelho')
            continue # continue para jogar de volta pro laço de repetição.
        except KeyboardInterrupt:
            texto('O usuário não informou o número.\n', 'vermelho')
            return 0
        else:
            return n


def menu(lista):
    print()
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        texto(f'{c} - ', 'amarelo')
        texto(f'{item}\n', 'azul')
        c += 1
    linha()
    opc = leiaInt('Sua Opção: ')
    return opc



