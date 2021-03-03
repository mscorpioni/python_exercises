"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""


def fatorial(num=1, show=False):
    """
    Calcula o fatorial de um número.
    :param num: o número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: o valor do Fatorial do número.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
    return f


print(fatorial(5, True))
help(fatorial)