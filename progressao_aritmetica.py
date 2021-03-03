"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""

num = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for i in range(10):
    print(f'{num}', end=' -> ')
    num += razao
print('Acabou')