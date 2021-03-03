"""
Lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
Ao término, pergunte para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
"""

num = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

termos = 10
cont = 0

while termos != 0:
    cont += termos
    i = 1
    while i <= termos:
        print(num, end=' -> ')
        i += 1
        num += razao
    print('Pausa')
    termos = int(input('\nQuantos termos você quer mostrar mais? '))
print(f'Programa encerrado com {cont} termos')