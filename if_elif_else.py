"""
Estrutura Condicional Aninhada:

if <condiçao1>:
    <bloco de comandos>
elif <condiçao2>:
    <bloco de comandos>
elif <condiçao3>:
    <bloco de comandos>
elif <condiçao4>:
    <bloco de comandos>
else:
    <bloco de comandos>
"""

nome = str(input('Digite seu nome: ')).title()
if nome == 'Mateus':
    print(f'Que nome bonito, {nome}!')
elif nome == 'João' or nome == 'Maria':
    print(f'{nome}, seu nome é bem popular no Brasil!')
elif 'Ana' in nome:
    print('Seu nome tem Ana!')
else:
    print(f'Que nome normal, {nome}!')
print('Tenha um bom dia!')