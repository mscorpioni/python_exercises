"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep
from operator import itemgetter

jogadas = {
    'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6)}

ranking = []

# A função 'itemgetter' ordena pela chave (0) ou pelo valor (1) do dicionário.
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

print(jogadas)
print(ranking)

# Uso o enumerate pois o ranking é uma lista
for i, j in enumerate(ranking):
    print(f'{i+1}o - {j[0]}: {j[1]} no dado.')
    sleep(0.5)