"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
"""

valor = float(input('Digite o valor das compras: R$ '))
print('''Formas de pagamento:
[1] À vista no dinheiro/cheque (10% off)
[2] À vista no cartão (5% off)
[3] Em 2x no cartão (sem desconto)
[4] Em 3x ou mais no cartão (5% de juros ao mês)''')
opcao = int(input('Qual opção? '))

if opcao == 1:
    print(f'Sua compra de R${valor:.2f} terá 10% de desconto e custará R${valor - (valor * 0.1):.2f}')
elif opcao == 2:
    print(f'Sua compra de R${valor:.2f} terá 5% de desconto e custará R${valor - (valor * 0.05):.2f}')
elif opcao == 3:
    print(f'Sua compra de R${valor:.2f} não terá desconto.')
elif opcao == 4:
    parcelas = int(input('Deseja parcelar em quantas vezes? '))
    print(f'Sua compra de R${valor:.2f} será parcelada em {parcelas}x de {(valor + parcelas * (valor * 0.05))/parcelas:.2f} e custará R${valor + parcelas * (valor * 0.05):.2f}')
else:
    print('Opção de pagamento inválida.')
