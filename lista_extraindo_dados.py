"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

lista = []
n1 = 0

while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break

lista.sort(reverse=True)

print(f'Você digitou {len(lista)} valores.')
print(f'Sua lista em forma decrescente é: {lista}')
if 5 in lista:
    print('Temos o 5 na lista.')
else:
    print('Não temos o 5 na lista.')
