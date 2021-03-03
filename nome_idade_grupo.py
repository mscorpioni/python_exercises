"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e sua idade, e quantas mulheres têm menos de 20 anos.
"""

media = 0.0
mais_velho = 0
nome_velho = ''
mulheres = 0

for p in range(1,5):
    nome = str(input(f'Digite o nome da {p}a pessoa: ')).strip().title()
    idade = int(input(f'Digite a idade da {p}a pessoa: '))
    sexo = str(input(f'Digite o sexo da {p}a pessoa (H/M): ')).lower()
    print()
    media += idade

    if idade > mais_velho and sexo == 'h':
        nome_velho = nome
        mais_velho = idade

    if sexo == 'm' and idade < 20:
        mulheres += 1

print(f'A média de idade do grupo é {media/4}')
print(f'O homem mais velho é {nome_velho} com {mais_velho} anos')
print(f'O grupo tem {mulheres} mulher(es) com menos de 20 anos')