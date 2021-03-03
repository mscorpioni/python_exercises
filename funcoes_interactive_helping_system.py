"""
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
Importante: use cores.
"""

cores = ('\033[m',         # 0 - Sem cor
         '\033[0;30;43m', # 1 - Amarelo
         '\033[7;30m'     # 2 - Branco
        )


def ajuda(com):
    print(cores[2])
    help(com)
    print(cores[0])


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)
    print(cores[0], end='')


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Função ou Biblioteca: (Fim para encerrar) '))
    if comando.upper() == 'FIM':
        break
    else:
        print('=' * 41)
        ajuda(comando)


titulo('Programa encerrado!', 1)
