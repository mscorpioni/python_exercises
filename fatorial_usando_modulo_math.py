"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
O Python tem uma função em math que calcula
"""

from math import factorial

num = int(input('Digite um número: '))
print(f'O fatorial de {num} é {factorial(num)}')