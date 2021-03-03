"""
Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""

mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for lin in range(3):
    for col in range(3):
        mat[lin][col] = int(input(f'Digite um valor para [{lin}, {col}]: '))

for lin in range(3):
    print('[ ', end='')
    for col in range(3):
        print(f'{mat[lin][col]:^5}', end=' ')
    print(']')
