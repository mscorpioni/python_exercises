"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues, na menor quantidade de possível.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

saque = int(input('Quanto deseja sacar? R$ '))

total = saque
valor_cedula = 50
qde_cedula = 0

while True:
    if total >= valor_cedula:
        total -= valor_cedula
        qde_cedula += 1
    else:
        if qde_cedula > 0:
            print(f'Total de {qde_cedula} de R${valor_cedula},00.')
        if valor_cedula == 50:
            valor_cedula = 20
        elif valor_cedula == 20:
            valor_cedula = 10
        elif valor_cedula == 10:
            valor_cedula = 1

        qde_cedula = 0
        if total == 0:
            break
