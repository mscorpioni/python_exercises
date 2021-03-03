"""
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

def maior(*num):
    print('-' * 50)
    print('Analisando os valores passados: ')
    print(num)
    print(f'Foram passados {len(num)} valores e o maior é {max(num)}')


maior(2, 3, 5, 10, 2)
maior(50, 3, 1, 0, 78, 4, 35, 6)
maior(6)
maior(10, -3, 2, 6, 54, 8, 76, 5, 65, 32, 12, 5, 77, 8, 9)