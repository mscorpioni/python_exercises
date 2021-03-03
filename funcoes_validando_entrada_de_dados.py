"""
Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante ‘a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
"""


def leiaInt(msg):
    numero = input(msg).strip()
    while not numero.isnumeric():
        print('Erro! Digite um número inteiro válido.')
        numero = input(msg).strip()
    return int(numero)


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')