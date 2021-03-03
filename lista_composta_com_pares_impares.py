"""
Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
"""

lista = [[], []]

for c in range(7):
    num = int(input(f'Digite o {c+1}o número: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
    print(lista)

lista[0].sort()
lista[1].sort()

print(f'Os números pares foram: {lista[0]}')
print(f'Os números ímpares foram: {lista[1]}')