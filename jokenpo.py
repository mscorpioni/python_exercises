from random import choice
from time import sleep

jogadas = ['Pedra', 'Papel', 'Tesoura']
empate = 0
ganhou = 0
perdeu = 0
jogador = '1'

while jogador != '0':
    jogador = str(input('Escolha Pedra, Papel ou Tesoura (0 para Sair):\n')).title()
    computador = choice(jogadas)
    print('JO', end=' ')
    sleep(0.5)
    print('KEN', end=' ')
    sleep(0.5)
    print('PO!!!')

    if jogador not in jogadas and jogador != '0':
        print('Jogada inválida!\n')
    elif (jogador == 'Papel' and computador == 'Pedra') or (jogador == 'Pedra' and computador == 'Tesoura') or (jogador == 'Tesoura' and computador == 'Papel'):
        print(f'{jogador} X {computador} = Ganhou!\n')
        ganhou += 1
    elif jogador == computador:
        print(f'{jogador} X {computador} = Empatou!\n')
        empate += 1
    elif jogador != '0':
        print(f'{jogador} X {computador} = Perdeu!\n')
        perdeu += 1

print(f'Jogo encerrado!\nGanhou {ganhou} vezes\nPerdeu {perdeu} vezes\nEmpatou {empate} vezes.')