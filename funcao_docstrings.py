'''
>> Docstrings: para documentar nossas funções
Basta eu abrir 3 aspas duplas logo após a declaração do nome da função. Ex:
def contador(i, f, p):
"""
<Texto da Documentação>
"""
Assim, quando outra pessoa utilizar a função e quiser saber o que ela faz, ela da um help(contador) e este texto é exibido.
'''


from time import sleep


def contagem(ini, fim, passo):
    """
    -> Faz uma contagem e mostra na tela.
    :param ini: início da contagem
    :param fim: fim da contagem
    :param passo: passo da contagem
    :return: sem retorno
    """
    print('-' * 30)
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}:')
    sleep(0.3)
    if passo == 0:
        passo = 1
    if ini < fim:
        if passo < 0:
            passo *= -1
        for i in range(ini, fim+1, passo):
            print(i, end=' ')
            sleep(0.3)
    else:
        if passo > 0:
            passo *= -1
        for i in range(ini, fim-1, passo):
            print(i, end=' ')
            sleep(0.3)
    print('FIM')
    sleep(0.3)


print('Exibindo a documentação da função contagem(): ')
help(contagem)
print('-' * 30)
print('Contagem personalizada ')
contagem(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
