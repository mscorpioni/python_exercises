"""
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes
"""

n1 = int(input('Digite o primeiro lado: '))
n2 = int(input('Digite o segundo lado: '))
n3 = int(input('Digite o terceiro lado: '))

if n1 + n2 < n3 or n1 + n3 < n2 or n2 + n3 < n1:
    print('Impossível criar um triângulos com estes segmentos!')
else:
    if n1 == n2 == n3:
        print('Estes segmentos formam um Triângulo Equilátero.')
    elif n1 != n2 and n2 != n3:
        print('Estes segmentos formam um Triângulo Escaleno.')
    else:
        print('Estes segmentos formam um Triângulo Isósceles.')
