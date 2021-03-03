"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

lista = []

while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valor duplicado! Não vou adicionar.')
    else:
        lista.append(n)
        print(f'Valor adicionado com sucesso: {lista}')

    continuar = str(input('Deseja continuar [S/N]? ')).upper()[0]
    if continuar == 'N':
        break

lista.sort()
print(f'Sua lista em ordem crescente é {lista}')
