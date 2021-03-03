"""
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint

num_pc = randint(0, 10)
num = 0
palpites = 0

print('Acabei de pensar em um número de 1 a 10.\nConsegue advinhar qual foi? ')
while num != num_pc:
    num = int(input('Qual seu palpite? '))
    palpites += 1
    if num > num_pc:
        print('Menos... Tente de novo.')
    elif num < num_pc:
        print('Mais... Tente de novo.')
print(f'Acertou com {palpites} palpites! Eu pensei no {num_pc} também!')

