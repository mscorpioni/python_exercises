"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""

lista = []
lista_impar = []
lista_par = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
    continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break

print(f'Lista Completa: {lista}')
print(f'Lista de pares: {lista_par}')
print(f'Lista de ímpares: {lista_impar}')

