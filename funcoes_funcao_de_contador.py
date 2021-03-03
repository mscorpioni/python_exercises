"""
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""

from time import sleep


def contagem(ini, fim, passo):
    print('-' * 30)
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}:')
    sleep(0.3)
    if passo == 0:
        passo = 1
    if ini < fim:
        if passo < 0:
            passo *= -1
        for i in range(ini, fim+1, passo):
            print(i, end=' ')
            sleep(0.3)
    else:
        if passo > 0:
            passo *= -1
        for i in range(ini, fim-1, passo):
            print(i, end=' ')
            sleep(0.3)
    print('FIM')
    sleep(0.3)


contagem(1, 10, 1)
contagem(10, 0, -2)

print('-'*30)
print('Contagem personalizada ')
contagem(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
