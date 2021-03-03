"""
Faça um programa que tenha uma lista chamada números
e duas funções chamadas sorteia() e somaPar().

A primeira função vai sortear 5 números e vai colocá-los dentro da lista
e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""
from random import randint
from time import sleep


def sorteia(l):
    cont = 0
    while cont < 5:
        num = randint(1, 10)
        if num not in l:
            l.append(num)
            sleep(0.3)
            print(num, end=' ')
            cont += 1


def somaPar(l):
    soma = 0
    for n in l:
        if n % 2 == 0:
            soma += n
    sleep(0.3)
    print(f'\nSomando os valores pares da lista {lista} temos {soma}', end='')


lista = []
print('Sorteando 5 valores da lista: ', end='')
sorteia(lista)
somaPar(lista)
