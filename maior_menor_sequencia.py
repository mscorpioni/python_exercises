"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
maior = 0
menor = 0

for n in range(1, 6):
    peso = float(input(f'Digite o peso da {n}a pessoa: '))
    if peso > maior:
        maior = peso
    if peso < menor or menor == 0:
        menor = peso
    print('maior: ', maior, ' / menor: ', menor)
print(f'O maior peso digitado foi {maior}Kg e o menor foi {menor}Kg')
