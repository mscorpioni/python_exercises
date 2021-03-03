"""
Escreva um programa que leia um número N inteiro qualquer e
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
"""


def fibonacci(n):
    a, b = 0, 1
    for i in range(a, n):
        print(a, end=' ')
        a, b = b, a + b


fibonacci(int(input('Quantos termos da Sequência de Fibonacci deseja calcular? ')))