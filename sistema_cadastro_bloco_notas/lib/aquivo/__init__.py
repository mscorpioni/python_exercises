from sistema_cadastro_bloco_notas.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # Escreve um arquivo de texto e (+) se não houver, crie.
    except:
        texto('Houve um erro na criação do arquivo!', 'vermelho')
    else:
        texto(f'O arquivo {nome} foi criado com sucesso!', 'amarelo')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        texto('Erro ao ler o arquivo!', 'vermelho')
    else:
        for linha in a: # Ler cada linha do arquivo
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<32}{dado[1]:>3} anos')


    finally:
        a.close()


def cadastrar(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at') # 'at' função para append no arquivo de texto. Já abre e adiciona dados.
    except:
        texto('Erro na abertura do arquivo!', 'vermelho')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            texto('Houve um erro ao escrever os dados!', 'vermelho')
        else:
            texto(f'Novo registro de {nome} adicionado!', 'amarelo')
