"""
Em Python não existe 'do while', mas dá para simular usando 'while True' e o 'break' para interromper o laço
"""

i = 0
while True:
    print(i)
    if i == 10:
        break
    i += 1

