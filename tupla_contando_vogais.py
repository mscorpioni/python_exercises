"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

"""

palavras = ('Mateus', 'Mog', 'Regina', 'Casa', 'Maringa', 'Cidade', 'Italia')

for item in palavras:

    print(f'Você digitou {item} e tem as vogais:', end=' ')
    for letra in item:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print()
