"""
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""
alunos = []
ficha = {}

while True:
    ficha['nome'] = str(input('Digite o nome: '))
    ficha['media'] = float(input(f'Digite a média de {ficha["nome"]}: '))
    if ficha['media'] >= 6:
        ficha['situacao'] = 'Aprovado'
    else:
        ficha['situacao'] = 'Reprovado'

    alunos.append(ficha.copy())
    ficha.clear()

    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break

print('='*20)
print(alunos)
print('='*20)
for cad in alunos:
    for k, v in cad.items():
        print(f'- {k.title()} é igual {v}')
    print('-'*10)

