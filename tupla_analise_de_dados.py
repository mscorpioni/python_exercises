"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

tupla = (int(input(f'Digite um valor: ')),
         int(input(f'Digite um valor: ')),
         int(input(f'Digite um valor: ')),
         int(input(f'Digite um valor: ')))
par = False

print(f'Você digitou os valores: {tupla}')

print(f'O valor 9 apareceu {tupla.count(9)} vezes')

print(f'O primeiro número 3 aparece na posição {tupla.index(3)+1}' if 3 in tupla else f'Você não digitou nenhum 3')

print('Os números pares foram: ', end='')
for num in tupla:
    if num % 2 == 0:
        par = True
        print(num, end=' ')
if not par:
    print('nenhum')
