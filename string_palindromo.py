"""
Crie um programa que leia uma frase qualquer (sem acentos) e diga se ela é um palíndromo, desconsiderando os espaços.
"""

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print(f'O inverso de {frase} é {inverso}')

if inverso == junto:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo')
