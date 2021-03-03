"""
Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.
"""

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Binário
[2] Octal
[3] Hexadecimal
''')
conversao = int(input('Opção: '))

if conversao == 1:
    print(f'O número {num} em Binário é {bin(num)[2:]}')    # [2:] para fatiar e exibir somente os caracteres de 2 em diante (remover o 0b, 0o e 0x)
elif conversao == 2:
    print(f'O número {num} em Octal é {oct(num)[2:]}')
elif conversao == 3:
    print(f'O número {num} em Hexadecimal é {hex(num)[2:]}')
else:
    print('Opção inválida.')