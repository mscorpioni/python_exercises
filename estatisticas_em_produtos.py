"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""

total = mais1000 = precobarato = 0
nomebarato = ''


while True:
    nome = str(input('Nome do produto: ')).title().strip()
    preco = float(input(f'Preço do produto {nome}: '))
    total += preco
    if preco > 1000:
        mais1000 += 1
    if preco <= precobarato or precobarato == 0:
        precobarato = preco
        nomebarato = nome

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Cadastrar mais produtos [S/N]? ')).strip().upper()[0]
    print('-'*20)
    if continuar == 'N':
        break

print(f'''
A) Total gasto na compra: R$ {total:.2f}.
B) {mais1000} produtos custam mais de R$ 1000,00.
C) {nomebarato} é o produto mais barato e custa {precobarato:.2f}.
''')