"""
Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
"""

n = int(input('Digite um número: '))
for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')
