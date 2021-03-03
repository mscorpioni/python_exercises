"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também
indique o menor e o maior valor que estão na tupla.
"""

from random import randint

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os números sorteados foram: ', end='')

for n in tupla:
    print(n, end=' ')

print(f'\nO maior valor sorteado é {max(tupla)} e o menor é {min(tupla)}')