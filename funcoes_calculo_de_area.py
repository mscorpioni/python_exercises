"""
Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e
mostre a área do terreno.
"""


def area(l, c):
    print(f'A área do terreno é {(l * c):.2f}m2.')


larg = float(input('Digite a largura: '))
comp = float(input('Digite o comprimento: '))
area(larg, comp)
