"""
Reescreva a função leiaInt(), incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""


def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('Erro! Por favor, digite um número inteiro válido.')
            continue # continue para jogar de volta pro laço de repetição.
        except KeyboardInterrupt:
            print('O usuário não informou o número.')
            return 0
        else:
            return numero


def leiaFloat(msg):
    while True:
        try:
            numero = float(input(msg))
        except (ValueError, TypeError):
            print('Erro! Por favor, digite um número real válido.')
            continue # continue para jogar de volta pro laço de repetição.
        except KeyboardInterrupt:
            print('O usuário não informou o número')
            return 0
        else:
            return numero


num = leiaInt('Digite um número inteiro: ')
num2 = leiaFloat('Digite o número real: ')
print(f'Você acabou de digitar o número inteiro {num} e o número real {num2}.')