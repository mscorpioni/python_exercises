"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = ' '

while sexo not in 'MF':
    sexo = str(input('Digite o sexo da pessoa (M/F): ')).strip().upper()[0]
    if sexo not in 'MF':
        print('Dados inválidos, digite novamente.')
print(f'Dados válidos. Sexo: {sexo}')