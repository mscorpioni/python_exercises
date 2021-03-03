"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""

pessoas = list()
dados = {}

while True:
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Erro! Responda apenas M ou F.')

    dados['idade'] = int(input('Idade: '))

    pessoas.append(dados.copy())
    dados.clear()

    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if continuar in 'Nn':
        break
print('-'*20)
print(pessoas)
print('-'*20)
print(f'A) Ao todo, temos {len(pessoas)} pessoas cadastradas.')

idade_total = 0
for i, v in enumerate(pessoas):
    idade_total += pessoas[i]['idade']
media_idade = idade_total / len(pessoas)
print(f'B) A média de idade é de {media_idade:.2f} anos.')

print('C) As mulheres cadastradas foram ', end='')
for pes in pessoas:
    if pes['sexo'] == 'F':
        print(f'{pes["nome"]}', end=' ')
print()
print('D) Lista de pessoas que estão acima da média:', end='')
for pes in pessoas:
    if pes['idade'] >= media_idade:
        print()
        for k, v in pes.items():
            print(f'{k.title()} = {v}; ', end='')
