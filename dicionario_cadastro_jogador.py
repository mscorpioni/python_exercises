"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

jogador = dict()
partidas = []

jogador['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for i in range(total):
    partidas.append(int(input(f'   Quantos gols na partida {i+1}? ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-'*20)
print(jogador)

print('-'*20)
for k, v in jogador.items():
    print(f'O campo {k.title()} tem valor {v}.')

print('-'*20)
print(f'O jogador {jogador["nome"]} jogou {total} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   Na partida {i+1} fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')