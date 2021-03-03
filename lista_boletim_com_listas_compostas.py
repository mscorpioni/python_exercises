"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e
permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

alunos = []
temp = []

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    alunos.append(temp[:])
    temp.clear()
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break

print('-'*30)
print(f"{'No.':<5}{'NOME':<20}{'MÉDIA':<5}")
print('-'*30)
for i, dado in enumerate(alunos):
    print(f'{i:<5}{alunos[i][0]:<20}{((alunos[i][1] + alunos[i][2]) / 2):>5.2f}', end='')
    print()

while True:
    print('-' * 30)
    cod = int(input('Mostrar notas de qual aluno? [999 para sair] '))
    if cod == 999:
        break
    else:
        if cod >= len(alunos):
            print(f'Código inválido. Tente novamente entre 0 e {len(alunos)-1}.')
        else:
            print(f'As notas de {alunos[cod][0]} são {alunos[cod][1]:.2f} e {alunos[cod][2]:.2f}.')
print('Programa encerrado.')