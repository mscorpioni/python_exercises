"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

lista = []

for i in range(5):
    lista.append(int(input(f'Digite o valor da posição {i}: ')))

print(lista)

maior = max(lista)
menor = min(lista)

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for pos, item in enumerate(lista):
    if item == maior:
        print(pos, end=' ')

print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for pos, item in enumerate(lista):
    if item == menor:
        print(pos, end=' ')

