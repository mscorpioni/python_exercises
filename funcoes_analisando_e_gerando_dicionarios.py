"""
Faça um programa que tenha uma função notas() que pode receber
várias notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A situação (opcional)
"""


def notas(*notas, sit=False):
    aluno = dict()
    aluno['total'] = len(notas)
    aluno['maior'] = max(notas)
    aluno['menor'] = min(notas)
    aluno['média'] = sum(notas) / len(notas)
    if sit:
        if aluno['média'] > 6:
            aluno['situação'] = 'BOA'
        else:
            aluno['situação'] = 'RUIM'
    return aluno


resp = notas(5, 2.1, 4, 10, sit=True)
print(resp)