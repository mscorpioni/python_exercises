# lib
from time import sleep

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


def cabecalho(msg, c='sem'):
    linha()
    print(msg.center(40))
    linha()


def linha(n=40):
    print('-' * n)


def menu():
    while True:
        cabecalho('MENU PRINCIPAL')
        texto('1 - ', 'amarelo')
        texto('Ver pessoas cadastradas\n', 'azul')
        texto('2 - ', 'amarelo')
        texto('Cadastrar nova pessoa\n', 'azul')
        texto('3 - ', 'amarelo')
        texto('Sair do sistema\n', 'azul')
        linha()

        try:
            texto('Sua opção: ', 'amarelo')
            op = int(input())
        except Exception as erro:
            texto(f'ERRO! {erro}\n', 'vermelho')
            sleep(1)
            continue
        else:
            if str(op) not in '123':
                texto('ERRO! Digite uma opção válida\n', 'vermelho')
                sleep(1)
                menu()
            else:
                cabecalho(op)
                sleep(1)
                menu()
            break
