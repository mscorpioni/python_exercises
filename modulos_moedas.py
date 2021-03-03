"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
from uteis import moedas

num = moedas.leiaDinheiro('Digite um valor: R$ ')

mais = int(input('Digite em quantos % quer aumentar: '))
menos = int(input('Digite em quantos % quer diminuir: '))
moedas.resumo(num, mais, menos)