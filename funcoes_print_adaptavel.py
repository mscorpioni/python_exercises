"""
Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
"""

def escreva(txt):
    tam = len(txt) + 2
    print('=' * tam)
    print(f'{txt:^{tam}}')
    print('=' * tam)


texto = str(input('Digite um texto: '))
escreva(texto)