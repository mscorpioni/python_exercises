"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

valor_imovel = float(input('Qual o valor do imóvel? R$ '))
salario = float(input('Qual seu salário? R$ '))
anos = int(input('Em quantos anos quer pagar? '))

meses = anos * 12
parcela = valor_imovel / meses

print(f'\nVocê está solicitando um financiamento de {meses} x R${parcela:.2f} cada parcela')

if parcela > salario * 0.3:
    print('Empréstimo Negado!')
else:
    print('Empréstimo Aprovado!')