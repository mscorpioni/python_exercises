"""
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date

nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} em {ano_atual}.')

if idade < 18:
    print(f'Ainda faltam {18-idade} ano(s) para seu alistamento.')
    print(f'Você se alistará em {nascimento+18}')
elif idade > 18:
    print(f'Você deveria ter se alistado há {idade-18} anos.')
    print(f'Seu alistamento foi em {nascimento+18}')
else:
    print('Você deve se alistar imediatamente!')