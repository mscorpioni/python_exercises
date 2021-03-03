"""
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint

venceu = 0

while True:
    num = -1
    jogada = ' '

    while not (0 <= num <= 10):
        num = int(input('Digite um número (0 a 10): '))
    while jogada not in 'PI':
        jogada = str(input('Par ou Ímpar (P/I): ')).upper().strip()[0]
    computador = randint(1, 10)
    print(f'Você jogou {num} e o computador {computador}. Total de {num + computador} = ', end='')
    soma = num + computador
    if soma % 2 == 0:
        print('PAR!')
    else:
        print('ÍMPAR!')
    if (jogada == 'P' and soma % 2 == 0) or (jogada == 'I' and soma % 2 != 0):
        print('Você venceu!\n')
        venceu += 1
    else:
        print('Você perdeu!\n')
        break

print(f'GAME OVER! Você venceu {venceu}', 'vez' if venceu <= 1 else 'vezes')