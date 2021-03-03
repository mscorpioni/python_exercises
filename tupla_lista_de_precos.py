"""
Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 4.2,
            'Transferidor', 6.8,
            'Caneta', 3.15
            )

print('-'*38)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print('-'*38)
for pos in range(len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')    # Formatando para preencher 30 espaços, com pontos, alinhando o item a esquerda
    else:
        print(f'R${listagem[pos]:>6.2f}')
print('-'*38)
