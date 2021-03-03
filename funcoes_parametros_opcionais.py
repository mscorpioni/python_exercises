"""
> Argumentos Opcionais: para dar mais dinamismo em funções Python
Eu já declaro o valor da variável na função. Assim, caso ela não receba um parâmetro, ela utiliza o que eu
declarei e não dá erro por falta de argumentos.
Eu posso declarar em uma variavel ou em todas.

"""

def soma(a, b, c=0):
    s = a + b + c
    print(f'A soma é {s}')


def multiplica(a, b=1):
    m = a * b
    print(f'A multiplicação é {m}')

soma(2, 3, 5)
soma(2, 3)

multiplica(3, 3)
multiplica(3)