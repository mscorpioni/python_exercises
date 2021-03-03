"""
Faça um programa que leia um número qualquer e mostre o seu fatorial (usando while)
"""

num = int(input('Digite um número: '))
fat = 1
n = num

while n > 0:
    fat *= n
    n -= 1

print(f'O fatorial de {num} é {fat}')