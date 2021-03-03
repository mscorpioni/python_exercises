"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

pessoas = []
temp = []
pesado = leve = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        pesado = leve = pessoas[0][1]
    else:
        if temp[1] > pesado:
            pesado = temp[1]
        if temp[1] < leve:
            leve = temp[1]

    pessoas.append(temp[:])
    temp.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break

print(pessoas)
print(f'Você cadastrou {len(pessoas)} pessoas.')

print(f'O maior peso foi {pesado:.2f}Kg de', end=' ')
for pes in pessoas:
    if pes[1] == pesado:
        print(pes[0], end=' ')
print(f'\nO menor peso foi {leve:.2f}Kg de', end=' ')
for pes in pessoas:
    if pes[1] == leve:
        print(pes[0], end=' ')
