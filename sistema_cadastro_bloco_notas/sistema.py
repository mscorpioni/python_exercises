# Programa principal

from time import sleep
from sistema_cadastro_bloco_notas.lib.interface import *
from sistema_cadastro_bloco_notas.lib.aquivo import *

# Abre o arquivo ficha.txt, criando o arquivo caso ainda não exista.
arq = 'ficha.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

itens_menu = ['Listar pessoas cadastradas',
              'Cadastrar nova pessoa',
              'Sair do sistema'
              ]

while True:
    resp = menu(itens_menu)
    if resp == 1:
        cabecalho('PESSOAS CADASTRADAS')
        lerArquivo(arq)
    elif resp == 2:
        cabecalho('CADASTRAR NOVA PESSOA')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho('Saindo do sistema...')
        break
    else:
        texto('Erro! Digite uma opção válida.\n', 'vermelho')
    sleep(1)
