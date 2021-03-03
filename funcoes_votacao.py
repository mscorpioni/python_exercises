"""
Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""


def voto(n):
    from datetime import date
    # Como eu só vou utilizar essa biblioteca dentro da função,
    # eu faço a importação dentro da função, assim ocupa menos memória.

    idade = date.today().year - n
    if idade < 16:
        return f'Com {idade} anos: Voto Negado.'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: Voto Obrigatório.'
    else:
        return f'Com {idade} anos: Voto Opcional.'


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))