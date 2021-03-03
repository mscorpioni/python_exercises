def teste(b):
    # Eu até posso declarar uma variável 'a' dentro da função.
    # Mas ela será local, e não a mesma da variável 'a' global.
    # Caso eu não declare uma variável local com o mesmo nome de uma global,
    # a global tem o valor que ela tem dentro do escopo local

    a = 8
    print(f'B dentro de teste vale {b}')
    b += 4
    print('Incrementando 4 em B dentro de teste...')
    print(f'B dentro de teste vale {b}')
    print(f'A dentro de teste vale {a}')


a = 5
print(f'A no programa principal vale {a}')
teste(a)
print(f'A no programa principal vale {a}')