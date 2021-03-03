"""
 Crie um programa que leia o ano de nascimento de sete pessoas.
 No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date

atual = date.today().year
maior = 0
menor = 0

for n in range(1, 8):
    nasc = int(input(f'Em que ano a {n}a pessoa nasceu? '))
    if atual - nasc >= 18:
        maior += 1
    else:
        menor +=1
print(f'Ao todo tivemos {maior} pessoas maior de idade, e {menor} menores')