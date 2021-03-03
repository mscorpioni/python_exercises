"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_3a_coluna = 0

for lin in range(3):
    for col in range(3):
        mat[lin][col] = int(input(f'Digite um valor para [{lin}, {col}]: '))

for lin in range(3):
    print('[ ', end='')
    for col in range(3):
        print(f'{mat[lin][col]:^5}', end=' ')
        if mat[lin][col] % 2 == 0:
            soma_pares += mat[lin][col]
        if col == 2:
            soma_3a_coluna += mat[lin][col]
    print(']')

print(f'A soma dos pares é: {soma_pares}')
print(f'A soma da 3a coluna é: {soma_3a_coluna}')
print(f'O maior valor da 2a linha é: {max(mat[1])}')