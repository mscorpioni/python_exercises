# Em dicionários, eu não posso dar o comando de fatiamento para criar uma cópia, como numa lista:
# ex: brasil.append(estado[:])
# Devo usar o método interno 'copy()'

estado = dict()
brasil = list()

for c in range(3):
    estado['uf'] = str(input('Estado: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())    # Copiando os Dicionários 'estado' para dentro da Lista 'brasil'
    estado.clear()
print(brasil)

for est in brasil:
    for k, v in est.items():
        print(k, v)

for est in brasil:
    for dado in est.values():
        print(dado, end=' ')
    print()
