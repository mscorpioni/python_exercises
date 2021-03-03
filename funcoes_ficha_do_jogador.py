"""
Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.
"""


def ficha(n='<Desconhecido>', g=0):
    return f'O jogador {n.title()} fez {g} gol(s) no campeonato.'


nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    print(ficha(g=gols))
else:
    print(ficha(nome, gols))
