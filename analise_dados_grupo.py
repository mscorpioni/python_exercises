"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.

No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""

maior18 = homem = mulher20 = 0


while True:
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        maior18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if sexo in 'M':
        homem += 1
    if sexo in 'F' and idade < 20:
        mulher20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    print()
    if continuar not in 'S':
        break
print(f'''- Pessoas com mais de 18 anos: {maior18}
- Homens cadastrados: {homem}
- Mulheres com menos de 20 anos: {mulher20}''')