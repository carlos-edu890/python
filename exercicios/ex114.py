'''
Exercício Python 114: Crie um código em Python que teste
se o site pudim está acessível pelo computador usado.
'''

from wsgiref.util import request_uri

from uteis import cor
from requests import get

try:
    response = get('https://www.pudim.com.br/')
except ModuleNotFoundError:
    print(f'\n{cor('Vermelho')}O site Pudim não está acessível no momento.\033[m')
else:
    print(f'\n{cor('Amarelo claro')}Conseguir acessar o site Pudim com sucesso.\033[m')