"""
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até 10.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

numeros = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco',\
          'seis', 'sete', 'oito', 'nove', 'dez'

while True:
    num = -1
    while not 0 <= num <= 10:
        num = int(input('Digite um número de 0 a 10: '))
    print(f'Você digitou o número {numeros[num]}')