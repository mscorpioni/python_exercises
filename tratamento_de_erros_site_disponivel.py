"""
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""

import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print(f'Deu erro! O site não está disponível no momento.')
else:
    print(f'Deu certo! {site.read()}')
