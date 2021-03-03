"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do Grêmio.
"""

times = 'Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Bahia'

print('Os 5 primeiros times: ', end='')
for pos, t in enumerate(times[0:5]):
    print(f'{pos+1}o: {t} /', end=' ')

print('\nOs últimos 4 colocados: ', end='')
for i in range(-4, 0):
    print(f'{times[i]} /', end=' ')

print('\nTimes em ordem alfabética: ', end='')
for t in sorted(times):
    print(t, end=' / ')


print(f"\nO Gêmio está na posição: {times.index('Grêmio')+1}")