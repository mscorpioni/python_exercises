"""
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

continuar = 's'
cont = media = maior = menor = 0

while continuar in 's':
    num = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? (S/N): ')).strip()[0]
    media += num
    cont += 1
    if num > maior:
        maior = num
    if num < menor or cont == 1:
        menor = num
print(f'Você digitou {cont} números e a média deles é {media/cont}')
print(f'O maior número foi {maior} e o menor {menor}')


