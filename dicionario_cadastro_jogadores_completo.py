"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# Aprimore o desafio, para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

time = list()
jogador = dict()
partidas = list()

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for i in range(total):
        partidas.append(int(input(f'   Quantos gols na partida {i+1}? ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)

    time.append(jogador.copy())
    jogador.clear()
    partidas.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break

print('-'*20)
print(time)

print('-'*50)
print(f'{"COD":<4}{"NOME":<20}{"GOLS":<20}{"TOTAL":<6}')
print('-'*50)
for i, v in enumerate(time):
    print(f'{i:<3} ', end='')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
    # print(f'{i:<4}{jog["nome"]:<20}{str(jog["gols"]):<20}{jog["total"]:<6}')
print('-'*50)

while True:
    opt = int(input('Mostrar dados de qual jogador? (999 interrompe) '))
    if opt == 999:
        break
    else:
        if opt not in range(len(time)):
            print('Código inválido. Digite novamente. ')
        else:
            print(f'Mostrando dados do jogador {time[opt]["nome"].upper()}:')
            for i, v in enumerate(time[opt]['gols']):
                print(f'   No jogo {i+1} fez {v} gols.')
            print(f'   Saldo de gols: {time[opt]["total"]}.')
            print('-' * 50)

print('<< Programa encerrado! >>')
