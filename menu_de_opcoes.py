"""
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

op = 0

while op != 5:
    op = int(input('''Digite uma opção: 
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Opção: '''))
    if op == 1:
        print('Somar')
    elif op == 2:
        print('Multiplicar')
    elif op == 3:
        print('Maior')
    elif op == 4:
        print('Novos números')
    elif op == 5:
        pass
    else:
        print('Opção inválida.')
print('Programa encerrado')